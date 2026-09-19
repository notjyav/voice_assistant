from abc import ABC, abstractmethod

class Skill(ABC):
    @abstractmethod
    def can_handle(self, query: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def handle(self,query: str) -> None:
        raise NotImplementedError