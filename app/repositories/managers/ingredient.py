from typing import Sequence

from ..managers import BaseManager
from ..models import Ingredient
from ..serializers import IngredientSerializer


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(
            cls.model._id.in_(set(ids))
        ).all() or []
