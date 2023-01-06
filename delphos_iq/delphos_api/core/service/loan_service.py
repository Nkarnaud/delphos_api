from dataclasses import dataclass
from typing import List

from delphos_api.core.entities import LoanEntity
from delphos_api.core.use_cases.loan_use_cases import (
    GetLoans,
    GetCountries,
    GetSectors,
    GetProject,
)
from delphos_api.infrastructure.adapters.repositories.loan_repository import DjangoLoanRepository


@dataclass
class LoanService:
    repository = DjangoLoanRepository()

    def get_loan(self) -> List[LoanEntity]:
        use_case = GetLoans(self.repository)
        loans = use_case.execute()
        return loans

    def get_country(self) -> List[str]:
        use_case = GetCountries(self.repository)
        countries = use_case.execute()
        return countries

    def get_sectors(self) -> List[str]:
        use_case = GetSectors(self.repository)
        sectors = use_case.execute()
        return sectors

    def get_project(self) -> List[str]:
        use_case = GetProject(self.repository)
        projects = use_case.execute()
        return projects
