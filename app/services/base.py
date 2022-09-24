from flask import jsonify

from app.common.base_factory import BaseFactory


class BaseService(BaseFactory):

    def __init__(
        self,
        controller,
    ):
        self.controller = controller

    def get_by_id(self, _id: int):
        result, error = self.controller.get_by_id(_id)
        return self.send_response(result, error)

    def get_all(self):
        result, error = self.controller.get_all()
        return self.send_response(result, error)

    def create(self, entry: dict):
        result, error = self.controller.create(entry)
        return self.send_response(result, error)

    def update(self, new_values: dict):
        result, error = self.controller.update(new_values)
        return self.send_response(result, error)

    def send_response(self, result, error):
        response = result if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code
