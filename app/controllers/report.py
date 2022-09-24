from sqlalchemy.exc import SQLAlchemyError
from typing import Any, Optional, Tuple

from ..repositories.managers import ReportManager


class ReportController:
    def __init__(self):
        self.manager = ReportManager()

    def get_all(self) -> Tuple[Any, Optional[str]]:
        try:
            top_ingredient = self.manager.get_top_ingredient()
            top_beverage = self.manager.get_top_beverage()
            top_3_customers = self.manager.get_top_3_customers()
            top_month = self.manager.get_top_month()
            return {
                'top_ingredient': top_ingredient,
                'top_beverage': top_beverage,
                'top_customers': top_3_customers,
                'top_month': top_month
            }, None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
