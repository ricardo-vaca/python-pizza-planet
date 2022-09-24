import pytest


def test_get_report_service(client, report_uri, create_orders):
    response = client.get(report_uri)
    pytest.assume(response.status.startswith('200'))

    returned_report = response.json
    pytest.assume(returned_report['top_ingredient'])
    pytest.assume(returned_report['top_beverage'])
    pytest.assume(returned_report['top_customers'])
    pytest.assume(returned_report['top_month'])
