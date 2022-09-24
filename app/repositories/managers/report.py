from sqlalchemy import func, desc, extract
import datetime

from ..models import Ingredient, OrderDetail, Beverage, Order
from ..serializers.order import OrderSerializer
from ...plugins import db


class ReportManager:
    serializer = OrderSerializer
    session = db.session

    @classmethod
    def get_top_ingredient(cls):
        serializer = cls.serializer(many=True)
        entry = cls.session.query(
            (Ingredient.name).label('name'),
            func.count(OrderDetail._id).label('total'),
        ).group_by(
            Ingredient.name
        ).join(
            OrderDetail
        ).limit(1)
        return serializer.dump(entry)[0]

    @classmethod
    def get_top_beverage(cls):
        serializer = cls.serializer(many=True)
        entry = cls.session.query(
            (Beverage.name).label('name'),
            func.count(OrderDetail._id).label('total'),
        ).group_by(
            Beverage.name
        ).join(
            OrderDetail
        ).limit(1)
        return serializer.dump(entry)[0]

    @classmethod
    def get_top_3_customers(cls):
        serializer = cls.serializer(many=True)
        entry = cls.session.query(
            Order.client_name,
            func.count(Order._id).label('total'),
        ).group_by(
            Order.client_name
        ).order_by(
            desc('total')
        ).limit(3)
        return serializer.dump(entry)

    @classmethod
    def get_top_month(cls):
        serializer = cls.serializer(many=True)
        entry = cls.session.query(
            extract('month', Order.date).label('name'),
            func.sum(Order.total_price).label('total')
        ).group_by(
            extract('month', Order.date)
        ).order_by(
            desc('total')
        ).limit(1)

        result = serializer.dump(entry)[0]
        result['name'] = datetime.date(
            year=2022,
            month=result['name'],
            day=1
        ).strftime('%B')
        result['total'] = "$" + str(round(result['total'], 2))

        return result
