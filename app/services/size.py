from flask import Blueprint, request

from app.common.http_methods import GET, POST, PUT

from .base import base_service
from ..controllers import SizeController

size = Blueprint('size', __name__)


@size.route('/', methods=GET)
def get_all():
    return base_service(
        SizeController,
        method=GET,
    )


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return base_service(
        SizeController,
        method=GET,
        id=_id
    )


@size.route('/', methods=POST)
def create_size():
    return base_service(
        SizeController,
        method=POST,
        request=request.json
    )


@size.route('/', methods=PUT)
def update_size():
    return base_service(
        SizeController,
        method=PUT,
        request=request.json
    )
