from typing import List

from ..managers import BaseManager
from ..models import Order, Ingredient, Beverage, OrderDetail
from ..serializers import OrderSerializer


class OrderManager(BaseManager):
    def __init__(self):
        super().__init__(model=Order, serializer=OrderSerializer)
        self.model = Order
        self.serializer = OrderSerializer

    def create(
        self, order_data: dict,
        ingredients: List[Ingredient],
        beverages: List[Beverage]
    ):
        new_order = self.model(**order_data)
        self.session.add(new_order)
        self.session.flush()
        self.session.refresh(new_order)
        self.session.add_all((OrderDetail(
            order_id=new_order._id,
            ingredient_id=ingredient._id,
            ingredient_price=ingredient.price
        )
            for ingredient in ingredients))
        self.session.add_all((OrderDetail(
            order_id=new_order._id,
            beverage_id=beverage._id,
            beverage_price=beverage.price
        )
            for beverage in beverages))
        self.session.commit()
        return self.serializer().dump(new_order)

    def update(self):
        raise NotImplementedError(f'Method not suported for {self.__name__}')
