from .base import BaseController
from ..repositories.managers import IngredientManager


class IngredientController(BaseController):
    def __init__(self):
        super().__init__(IngredientManager)
