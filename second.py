import pytest

from application import Application


@pytest.fixture()
def app():
    fixture = Application()
    # request.addfinalizer(fixture)
    return fixture


def test_first(app):
    app.login(username="administrator", password="5ecr3t")
