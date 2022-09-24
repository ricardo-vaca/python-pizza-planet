from flask import Blueprint, request

from app.common.http_methods import GET, POST, PUT

from .base import BaseService
from ..controllers import BeverageController

beverage = Blueprint('beverage', __name__)


@beverage.route('/', methods=GET)
def get_beverages():
    return BaseService(
        BeverageController(),
    ).get_all()


@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    return BaseService(
        BeverageController(),
    ).get_by_id(_id)


@beverage.route('/', methods=POST)
def create_beverage():
    return BaseService(
        BeverageController(),
    ).create(request.json)


@beverage.route('/', methods=PUT)
def update_beverage():
    return BaseService(
        BeverageController(),
    ).update(request.json)
