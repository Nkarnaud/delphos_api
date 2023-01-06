from dataclasses import dataclass

from uuid import UUID


@dataclass
class LoanEntity:
    uuid: UUID
    title: str
    country: str
    sector: str
    amount: str
