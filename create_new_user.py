import pytest

from application import Application


@pytest.fixture()
def app():
    fixture = Application()
    return fixture


def test_create_new_user(app):
    app.login(username="administrator", password="5ecr3t")
    app.open_users_page()