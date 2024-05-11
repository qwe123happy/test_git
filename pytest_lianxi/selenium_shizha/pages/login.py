from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium_shizha.base.basepage import Wait
from selenium import webdriver
from pytest_lianxi.selenium_shizha.logs.default import Mylogs


class LoginPages:

    username_locator=(10,(By.XPATH, '//*[@id="loginname"]'))
    password_locator =(10,(By.XPATH, '//*[@id="nloginpwd"]'))
    button_locator=(10,(By.XPATH, '//*[@id="loginsubmit"]'))

    def __init__(self,driver):
        self.driver = driver
        ##引入等待模块
        self.wait = Wait(self.driver)
        #
        self.username=LoginPages.username_locator
        self.password=LoginPages.password_locator
        self.button=LoginPages.button_locator
        self.logger = Mylogs()

##定位用户账号输入框元素
    def get_userinfo_element(self):
        ##不适用继承
        self.userinfo_element=self.wait.wait_element_located(self.username[0],self.username[1])
        ##使用继承，继承basepage中的wait类  待调试
        # self.userinfo_element=self.wait_element_located(self.username[0],self.username[1])
        return self.userinfo_element


##定位用户密码输入框元素
    def get_password_element(self):
        self.password_element=self.wait.wait_element_located(self.password[0],self.password[1])
        # self.password_element=self.wait_element_located(self.password[0],self.password[1])
        return self.password_element

##登录，提交用户信息
    def submit_userinfo(self, phone, password):

        username_element= self.get_userinfo_element()

        pwd_element=self.get_password_element()

##定位登录按钮
        # button_element = WebDriverWait(self.driver, self.button[0]).until(
        #     ec.element_to_be_clickable(self.button[1]))

        button_element=self.wait.wait_element_clicked(self.button[0],self.button[1])
        # button_element=self.wait_element_clicked(self.button[0],self.button[1])

        # 提交登录信息
        username_element.send_keys(phone)  ##15603389663
        pwd_element.send_keys(password)  ## cb698754*
        try:
            button_element.click()
        except Exception :
            # print("Element is not clickable !!!")
            self.logger.logs('ERROR',"Element is not clickable !!!")

##执行下一个用例前，清空输入框
    def userinfo_clear(self):
        return self.get_userinfo_element().clear()

    def password_clear(self):
        return self.get_password_element().clear()

##断言元素定位

    # def decide_element(self):
    #     return True
