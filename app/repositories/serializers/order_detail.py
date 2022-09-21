from app.plugins import ma

from ..models import OrderDetail
from ..serializers import IngredientSerializer, BeverageSerializer


class OrderDetailSerializer(ma.SQLAlchemyAutoSchema):

    ingredient = ma.Nested(IngredientSerializer)
    beverage = ma.Nested(BeverageSerializer)

    class Meta:
        model = OrderDetail
        load_instance = True
        fields = (
            'ingredient_price',
            'ingredient',
            'beverage_price',
            'beverage'
        )
