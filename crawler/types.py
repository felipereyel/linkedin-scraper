from typing import Optional
from dataclasses import dataclass


@dataclass
class CompanyInput:
    name: str

    def out_success(self, link: str) -> "CompanyOutput":
        return CompanyOutput(link=link, status="OK", name=self.name, error=None)

    def out_error(self, error: str) -> "CompanyOutput":
        return CompanyOutput(error=error, status="ERROR", name=self.name, link=None)


@dataclass
class CompanyOutput:
    name: str
    status: str
    link: Optional[str]
    error: Optional[str]

    @property
    def is_success(self) -> bool:
        return self.status == "OK"

    def to_csv(self) -> str:
        return f"{self.name},{self.status},{self.link or ''}\n"
