import time, datetime
from typing import List
from progress.bar import Bar
from playwright.sync_api import sync_playwright, Page, Playwright

from .utils import extract_number
from .types import CompanyInput, CompanyOutput
from .errors import LoginError, SearchError, EmployeeError

LINKEDIN_URL = "https://www.linkedin.com"
LOGIN_URL = f"{LINKEDIN_URL}/login"
FEED_URL = f"{LINKEDIN_URL}/feed/"
SEARCH_URL = f"{LINKEDIN_URL}/search/results/companies/?keywords="


def check_login(page: Page) -> bool:
    page.goto(FEED_URL)
    return "login" not in page.title().lower()


def await_login(p: Playwright) -> Page:
    page = p.chromium.launch(headless=False).new_page()
    page.goto(LOGIN_URL)

    max_wait = 100
    start = datetime.datetime.now()
    while True:
        try:
            if "login" not in page.title().lower():
                break
        except:
            if check_login(page):
                break

        if (datetime.datetime.now() - start).seconds > max_wait:
            raise LoginError()

        time.sleep(1)

    return page


def find_company_link(page: Page, name: str) -> str:
    page.goto(SEARCH_URL + name)
    # page.wait_for_load_state("domcontentloaded")

    r = page.wait_for_selector(".entity-result")
    if not r:
        raise SearchError()

    try:
        return r.query_selector("a").get_attribute("href")
    except:
        raise SearchError()


def find_company_employees(page: Page, link: str) -> int:
    page.goto(link + "people/")

    r = page.wait_for_selector(".org-people__header-spacing-carousel")
    if not r:
        raise EmployeeError()

    try:
        txt_content = r.query_selector("h2").inner_text()
        return extract_number(txt_content)
    except:
        raise EmployeeError()


def run(inputs: List[CompanyInput]) -> List[CompanyOutput]:
    with sync_playwright() as p:
        with Bar("Processing", max=len(inputs)) as bar:
            page = await_login(p)

            outputs = []
            for company in inputs:
                out = company.process_output()
                try:
                    out.link = find_company_link(page, company.name)
                    out.employees = find_company_employees(page, out.link)
                    out.status = "OK"
                except Exception as e:
                    out.error = str(e)
                    out.status = "ERROR"
                finally:
                    outputs.append(out)
                    bar.next()

            return outputs
