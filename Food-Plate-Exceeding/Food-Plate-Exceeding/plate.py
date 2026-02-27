
from abc import ABC, abstractmethod


class Plate(ABC):

    @abstractmethod
    def description(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def area(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def weight(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def count(self) -> int:
        raise NotImplementedError
