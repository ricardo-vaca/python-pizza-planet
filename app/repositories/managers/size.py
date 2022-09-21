from ..managers import BaseManager
from ..models import Size
from ..serializers import SizeSerializer


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer
