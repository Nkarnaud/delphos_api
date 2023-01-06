from dataclasses import dataclass
from typing import List

from delphos_api.core.entities import LoanEntity
from delphos_api.core.use_cases.interfaces.loan_interface import LoanRepositoryInterface
from delphos_api.core.use_cases.interfaces.use_case_interface import UseCaseInterface


@dataclass
class GetLoans(UseCaseInterface):
    repository: LoanRepositoryInterface

    def execute(self) -> List[LoanEntity]:
        return self.repository.loans()


@dataclass
class GetCountries(UseCaseInterface):
    repository: LoanRepositoryInterface

    def execute(self) -> List[str]:
        return self.repository.get_countries()


@dataclass
class GetSectors(UseCaseInterface):
    repository: LoanRepositoryInterface

    def execute(self) -> List[str]:
        return self.repository.get_sectors()


@dataclass
class GetProject(UseCaseInterface):
    repository: LoanRepositoryInterface

    def execute(self) -> List[str]:
        return self.repository.get_projects()
