import pytest
from pytest_lianxi.selenium_shizha.conftest import my_setup_class

@pytest.fixture
def init_setup(my_setup_class):
    driver, home_page, login_page = my_setup_class  # 从元组中提取需要的对象

    yield login_page

    login_page.userinfo_clear()
    login_page.password_clear()