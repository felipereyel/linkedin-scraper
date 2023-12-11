import time, datetime
from typing import List
from progress.bar import Bar
from playwright.sync_api import sync_playwright, Page, Playwright

from .types import CompanyInput, CompanyOutput

LINKEDIN_URL = "https://www.linkedin.com"
LOGIN_URL = f"{LINKEDIN_URL}/login"
FEED_URL = f"{LINKEDIN_URL}/feed/"
SEARCH_URL = f"{LINKEDIN_URL}/search/results/companies/?keywords="


class LoginError(Exception):
    def __init__(self) -> None:
        super().__init__("Login failed")


class SearchError(Exception):
    def __init__(self) -> None:
        super().__init__("Search failed")


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


def scrape_one_company(page: Page, name: str) -> str:
    page.goto(SEARCH_URL + name)

    r = page.query_selector(".entity-result")
    if not r:
        raise SearchError()

    return r.query_selector("a").get_attribute("href")


def scraper(inputs: List[CompanyInput]) -> List[CompanyOutput]:
    with sync_playwright() as p:
        with Bar("Processing", max=len(inputs)) as bar:
            page = await_login(p)

            outputs = []
            for company in inputs:
                try:
                    link = scrape_one_company(page, company.name)
                    outputs.append(company.out_success(link))
                except Exception as e:
                    outputs.append(company.out_error(str(e)))
                finally:
                    bar.next()

            return outputs
