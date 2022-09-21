from flask import Blueprint, jsonify, request

from app.common.http_methods import GET, POST, PUT

from .base import base_service
from ..controllers import IngredientController

ingredient = Blueprint('ingredient', __name__)


@ingredient.route('/', methods=GET)
def get_ingredients():
    return base_service(
        IngredientController,
        method=GET,
    )


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return base_service(
        IngredientController,
        method=GET,
        id=_id,
    )


@ingredient.route('/', methods=POST)
def create_ingredient():
    return base_service(
        IngredientController,
        method=POST,
        request=request.json
    )


@ingredient.route('/', methods=PUT)
def update_ingredient():
    return base_service(
        IngredientController,
        method=PUT,
        request=request.json
    )
