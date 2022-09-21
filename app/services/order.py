from flask import Blueprint, request

from app.common.http_methods import GET, POST

from .base import base_service
from ..controllers import OrderController

order = Blueprint('order', __name__)


@order.route('/', methods=GET)
def get_orders():
    return base_service(
        OrderController,
        method=GET
    )


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return base_service(
        OrderController,
        method=GET,
        id=_id,
    )


@order.route('/', methods=POST)
def create_order():
    return base_service(
        OrderController,
        method=POST,
        request=request.json
    )
