from ..managers import BaseManager
from ..models import Size
from ..serializers import SizeSerializer


class SizeManager(BaseManager):
    def __init__(self):
        super().__init__(model=Size, serializer=SizeSerializer)
        self.model = Size
