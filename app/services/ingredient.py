from flask import Blueprint, request

from app.common.http_methods import GET, POST, PUT

from .base import BaseService
from ..controllers import IngredientController

ingredient = Blueprint('ingredient', __name__)


@ingredient.route('/', methods=GET)
def get_ingredients():
    return BaseService(
        IngredientController(),
    ).get_all()


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return BaseService(
        IngredientController(),
    ).get_by_id(_id)


@ingredient.route('/', methods=POST)
def create_ingredient():
    return BaseService(
        IngredientController(),
    ).create(request.json)


@ingredient.route('/', methods=PUT)
def update_ingredient():
    return BaseService(
        IngredientController(),
    ).update(request.json)
