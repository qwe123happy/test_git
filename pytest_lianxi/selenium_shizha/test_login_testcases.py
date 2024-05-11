import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_shizha.pages.login import LoginPages
from selenium_shizha.datas import login
from selenium_shizha.pages.home import HomePages
from pytest_lianxi.selenium_shizha.init_setup_test import init_setup
from pytest_lianxi.selenium_shizha.logs.default import Mylogs
import pytest  ##pytest 兼容unittest


##pytest会自动寻找测试用例执行，规则文件名以test开头或结尾。 文件内的方法名必须以test开头

###fixture   环境管 理工具   @pytest.fixture   不能与unittest  ddt一起使用。会发生冲突
###yield    生成器



@pytest.mark.usefixtures('my_setup_class')
class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.parametrize('datas', login.login_data_success)
    @pytest.mark.usefixtures('init_setup')
    def test_login_in_success(self, datas, my_setup_class):
        ##登录
        driver, home_page, login_page = my_setup_class
        login_page.submit_userinfo(datas['username'], datas['password'])  ##分层思想，登录页面行为。登录封装成一个类，方便调用

        ##优化，断言所需要的元素定位是在首页发生的，属于首页行为。封装定位用户姓名元素的操作，方便引用
        try:
            assert datas['expected'] == HomePages(driver).get_username()
        except Exception as e:
            Mylogs().logs('INFO', e)
            raise e

    @pytest.mark.parametrize('datas', login.login_data_error)
    @pytest.mark.usefixtures('init_setup')
    def test_login_in_error(self, datas, my_setup_class):
        # self.login_page.submit_userinfo(self.driver,'465552','DS36523')
        driver, home_page, login_page = my_setup_class
        login_page.submit_userinfo(phone=datas['username'], password=datas['password'])

        time.sleep(5)

        ##定位拖动滑块的位置
        slider = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')))

        slider_width = slider.size['width']

        ##定位背景图像的位置
        background = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(
                (By.XPATH, '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[1]/img')))

        background_width = background.size['width']

        # 计算滑块需要移动的距离（示例中直接将滑块移动到背景图像的最右边）
        distance = background_width - slider_width

        # 模拟拖动滑块的操作
        action = ActionChains(driver)
        action.click_and_hold(slider).move_by_offset(distance, 0).release().perform()

        # 等待验证结果
        time.sleep(3)  # 等待验证结果加载，可以根据实际情况调整等待时间

        # 验证结果（示例中简单输出）
        if WebDriverWait(driver, 10).until(
                ec.visibility_of_element_located(
                    (By.XPATH, '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]'))):  # 替换成验证成功的提示信息
            Mylogs().logs('EEEOR', "拼图验证失败！")
        else:
            Mylogs().logs('INFO', "拼图验证成功！")

    ### @pytest.mark.usefixtures('方法名method') 由于pytest与unittest中部分方法冲突，则使用该种方法。代替setup的作用
    @pytest.mark.parametrize('datas', login.login_data_empty)  ##pytest中的ddt
    @pytest.mark.usefixtures('init_setup')
    @pytest.mark.regression
    def test_login_in_empty(self, datas, my_setup_class):
        driver, home_page, login_page = my_setup_class  ##要配合yield使用， yield 参数1，参数2    yield在fixture中使用
        login_page.submit_userinfo(datas['username'], datas['password'])
        try:
            assert datas['expected'] == '3'
        except Exception as e:
            logger=Mylogs()
            logger.logs('ERROR', e)


