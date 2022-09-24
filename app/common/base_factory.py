from abc import ABC, abstractmethod
from typing import Any


class BaseFactory(ABC):
    @abstractmethod
    def get_by_id(self, _id: int) -> Any:
        pass

    @abstractmethod
    def get_all(self) -> Any:
        pass

    @abstractmethod
    def create(self, entry: dict):
        pass

    @abstractmethod
    def update(self, new_values: dict) -> Any:
        pass
