from sqlalchemy.exc import SQLAlchemyError
from typing import Any, Optional, Tuple

from ..repositories.managers import ReportManager


class ReportController:
    manager = ReportManager

    @classmethod
    def get_all(cls) -> Tuple[Any, Optional[str]]:
        try:
            top_ingredient = cls.manager.get_top_ingredient()
            top_beverage = cls.manager.get_top_beverage()
            top_3_customers = cls.manager.get_top_3_customers()
            top_month = cls.manager.get_top_month()
            return {
                'top_ingredient': top_ingredient,
                'top_beverage': top_beverage,
                'top_customers': top_3_customers,
                'top_month': top_month
            }, None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
