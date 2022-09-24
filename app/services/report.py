from flask import Blueprint, jsonify

from app.common.http_methods import GET

from ..controllers import ReportController
from ..services.base import base_service

report = Blueprint('report', __name__)


@report.route('/', methods=GET)
def get_report():
    return base_service(
        ReportController,
        method=GET
    )
