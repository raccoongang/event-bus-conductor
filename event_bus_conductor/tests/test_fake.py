"""
Fake test for pass test by CI/CD
"""


def test_pass(json_response):
    assert json_response.status_code == 200
    assert isinstance(json_response.message, str)


def test_fail(false_json_response):
    assert false_json_response.status_code == 400
