import pytest
import time

from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    return fixture


def test_create_new_user(app):
    app.login(username="administrator", password="5ecr3t")
    #app.navigate_to_submenu_element(elementid=2, submenu_title="Пользователи")
    app.new_user_name()
    #app.click_on_button_in_toolbar_by_id(0)
    #time.sleep(10)
