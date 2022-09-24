from flask import Blueprint

from app.common.http_methods import GET

from ..controllers import ReportController
from ..services.base import BaseService

report = Blueprint('report', __name__)


@report.route('/', methods=GET)
def get_report():
    return BaseService(
        ReportController(),
    ).get_all()
