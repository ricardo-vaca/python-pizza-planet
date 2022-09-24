from .base import BaseController
from ..repositories.managers import SizeManager


class SizeController(BaseController):
    def __init__(self):
        super().__init__(SizeManager)
