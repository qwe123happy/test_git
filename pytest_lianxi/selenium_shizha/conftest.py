import pytest
from selenium import webdriver
import time
from pytest_lianxi.selenium_shizha.pages.home import HomePages
from pytest_lianxi.selenium_shizha.pages.login import LoginPages


@pytest.fixture(scope='class')
def my_setup_class():
    driver = webdriver.Edge()
    url = 'https://www.jingdong.com'
    driver.get(url)
    time.sleep(5)
    driver.refresh()
    driver.maximize_window()


    home_page = HomePages(driver)  ##实例化首页行为的类，传入driver
    home_page.click_login_location()  ##调用点击‘请先登录’按钮方法

    login_page = LoginPages(driver)  ##实例化对象，并把driver参数传进去
    # cls.login_page=LoginPages()
    # result=home_page.get_username().text   ##调用获取用户名称元素的方法

    yield driver,home_page,login_page

    driver.quit()