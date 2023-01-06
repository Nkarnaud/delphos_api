from typing import List

from django.db.models import QuerySet

from delphos_api.core.entities import LoanEntity
from delphos_api.core.use_cases.interfaces.loan_interface import LoanRepositoryInterface
from delphos_api.models import Loans


class DjangoLoanRepository(LoanRepositoryInterface):

    def get_countries(self) -> List[str]:
        return Loans.objects.values('country')

    def get_sectors(self) -> List[str]:
        return Loans.objects.values('sector')

    def get_projects(self) -> List[str]:
        return Loans.objects.values('title')

    def loans(self) -> List[QuerySet]:
        return Loans.objects.all()

    @staticmethod
    def _factory_loan(loan: Loans) -> LoanEntity:
        if loan:
            return LoanEntity(
                Loans.uuid,
                loan.country,
                loan.title,
                loan.sector,
                loan.amount
            )

