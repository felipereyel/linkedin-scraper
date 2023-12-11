import json
from typing import List
from pathlib import Path

from .types import CompanyInput, CompanyOutput


def read_input(i: str) -> List[CompanyInput]:
    input_path = Path(i)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file {i} not found")

    with input_path.open() as f:
        return [CompanyInput(name=line.strip()) for line in f.readlines()]


def write_output(o: str, companies: List[CompanyOutput]) -> None:
    output_path = Path(o)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w") as f:
        for company in companies:
            if not company.is_success:
                print(f"Error scraping {company.name}: {company.error}")
            f.write(company.to_csv_row() + "\n")
