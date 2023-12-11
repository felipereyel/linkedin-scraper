from typing import Optional
from dataclasses import dataclass


@dataclass
class CompanyInput:
    name: str

    def process_output(self) -> "CompanyOutput":
        return CompanyOutput(
            name=self.name, status="PROCESSING", link=None, employees=None, error=None
        )


@dataclass
class CompanyOutput:
    name: str
    status: str
    link: Optional[str]
    employees: Optional[int]
    error: Optional[str]

    @property
    def is_success(self) -> bool:
        return self.status == "OK"

    def to_csv_row(self) -> str:
        return f"{self.name},{self.status},{self.link or ''},{self.employees or ''}"
