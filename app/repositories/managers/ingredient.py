from typing import Sequence

from ..managers import BaseManager
from ..models import Ingredient
from ..serializers import IngredientSerializer


class IngredientManager(BaseManager):
    def __init__(self):
        super().__init__(model=Ingredient, serializer=IngredientSerializer)
        self.model = Ingredient

    def get_by_id_list(self, ids: Sequence):
        return self.session.query(self.model).filter(
            self.model._id.in_(set(ids))
        ).all() or []
