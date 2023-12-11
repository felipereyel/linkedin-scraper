import json
from typing import List
from pathlib import Path

from .types import CompanyInput, CompanyOutput


def read_input(inpt: str) -> List[CompanyInput]:
    input_path = Path(inpt)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file {inpt} not found")

    with input_path.open() as f:
        return [CompanyInput(name=line.strip()) for line in f.readlines()]


def write_output(outpt: str, companies: List[CompanyOutput]) -> None:
    output_path = Path(outpt)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w") as f:
        for company in companies:
            if not company.is_success:
                print(f"Error crawling {company.name}: {company.error}")
            f.write(company.to_csv())
