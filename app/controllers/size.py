from .base import BaseController
from ..repositories.managers import SizeManager


class SizeController(BaseController):
    manager = SizeManager
