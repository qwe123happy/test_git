from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class HomePages:
    def __init__(self,driver):
        self.driver = driver


    def login_location(self):
        return  WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="ttbar-login"]/a[1]/span[2]')))  ##定位跳转登录页面按钮

    def click_login_location(self):
        self.login_location().click()

    ## 登录成功后，定位已登录的用户昵称.这个行为属于首页的行为
    def get_username(self) :
        try:
            e=WebDriverWait(self.driver,20).until(
            ec.visibility_of_element_located((By.XPATH,'//*[@id="ttbar-login"]/div[1]/a')))
            return e.text
        except:
            return False