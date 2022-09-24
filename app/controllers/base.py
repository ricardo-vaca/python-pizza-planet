from typing import Any, Optional, Tuple
from sqlalchemy.exc import SQLAlchemyError


from app.common.base_factory import BaseFactory
from ..repositories.managers import BaseManager


class BaseController(BaseFactory):
    def __init__(self, manager: Optional[BaseManager] = None):
        self.manager = manager

    def get_by_id(self, _id: Any) -> Tuple[Any, Optional[str]]:
        try:
            return self.manager().get_by_id(_id), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    def get_all(self) -> Tuple[Any, Optional[str]]:
        try:
            return self.manager().get_all(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    def create(self, entry: dict) -> Tuple[Any, Optional[str]]:
        try:
            return self.manager().create(entry), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)

    def update(self, new_values: dict) -> Tuple[Any, Optional[str]]:
        try:
            _id = new_values.pop('_id', None)
            if not _id:
                return None, 'Error: No id was provided for update'
            return self.manager().update(_id, new_values), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
