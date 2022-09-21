from .base import BaseController
from ..repositories.managers import IngredientManager


class IngredientController(BaseController):
    manager = IngredientManager
