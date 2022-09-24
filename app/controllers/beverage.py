from .base import BaseController
from ..repositories.managers import BeverageManager


class BeverageController(BaseController):
    def __init__(self):
        super().__init__(BeverageManager)
