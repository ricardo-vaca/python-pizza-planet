from flask import Blueprint, request

from app.common.http_methods import GET, POST, PUT

from .base import BaseService
from ..controllers import SizeController

size = Blueprint('size', __name__)


@size.route('/', methods=GET)
def get_all():
    return BaseService(
        SizeController(),
    ).get_all()


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return BaseService(
        SizeController(),
    ).get_by_id(_id)


@size.route('/', methods=POST)
def create_size():
    return BaseService(
        SizeController(),
    ).create(request.json)


@size.route('/', methods=PUT)
def update_size():
    return BaseService(
        SizeController(),
    ).update(request.json)
