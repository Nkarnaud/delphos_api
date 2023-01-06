import abc
from typing import List

from delphos_api.core.entities import LoanEntity


class LoanRepositoryInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_countries(self) -> List[str]:
        ...

    @abc.abstractmethod
    def get_sectors(self) -> List[str]:
        ...

    @abc.abstractmethod
    def get_projects(self) -> List[str]:
        ...

    @abc.abstractmethod
    def loans(self) -> List[LoanEntity]:
        ...
