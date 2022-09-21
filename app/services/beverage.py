from flask import Blueprint, request

from app.common.http_methods import GET, POST, PUT

from .base import base_service
from ..controllers import BeverageController

beverage = Blueprint('beverage', __name__)


@beverage.route('/', methods=GET)
def get_beverages():
    return base_service(
        BeverageController,
        method=GET
    )


@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    return base_service(
        BeverageController,
        method=GET,
        id=_id,
    )


@beverage.route('/', methods=POST)
def create_beverage():
    return base_service(
        BeverageController,
        method=POST,
        request=request.json
    )


@beverage.route('/', methods=PUT)
def update_beverage():
    return base_service(
        BeverageController,
        method=PUT,
        request=request.json
    )
