import pytest

from app.controllers.report import ReportController


def test_get_report(app, create_orders):
    created_report, error = ReportController.get_all()
    pytest.assume(error is None)
    for param, value in created_report.items():
        pytest.assume(value == created_report[param])
        pytest.assume(created_report['top_ingredient'])
        pytest.assume(created_report['top_beverage'])
        pytest.assume(created_report['top_customers'])
        pytest.assume(created_report['top_month'])
