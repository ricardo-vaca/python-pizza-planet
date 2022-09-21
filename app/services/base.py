from flask import jsonify, Request
from typing import Optional

from app.common.http_methods import GET, POST, PUT


def base_service(
    Controller,
    method,
    request: Optional[Request] = None,
    id: Optional[int] = None
):
    result, error = Controller.get_by_id(id) if id \
        else Controller.get_all() if method == GET \
        else Controller.create(request) if method == POST \
        else Controller.update(request) if method == PUT \
        else None

    response = result if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code
