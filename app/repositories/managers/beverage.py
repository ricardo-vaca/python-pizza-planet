from typing import Sequence

from ..managers import BaseManager
from ..models import Beverage
from ..serializers import BeverageSerializer


class BeverageManager(BaseManager):
    def __init__(self):
        super().__init__(model=Beverage, serializer=BeverageSerializer)
        self.model = Beverage

    def get_by_id_list(self, ids: Sequence):
        return self.session.query(self.model).filter(
            self.model._id.in_(set(ids))
        ).all() or []
