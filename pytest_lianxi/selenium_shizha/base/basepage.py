from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver import Edge
import time



logging.basicConfig(filename='D:\pycharm code\py-selenium\selenium_shizha\logs\default.log',encoding='utf-8',level='INFO')
logger=logging.getLogger()
class Wait:
    def __init__(self,driver:Edge):
        self.driver=driver


    def wait_element_located(self,space=10,tuple=None) -> WebElement:
        try:
            return WebDriverWait(self.driver,space).until(ec.visibility_of_element_located(tuple))
        except Exception as e:
            print('等待元素出现超时，错误{}'.format(e))
            logger.error('出现错误,打印日志')
            self.driver.save_screenshot('D:\pycharm code\py-selenium\selenium_shizha\logs\{}.jpg'.format(time.time()))

    def wait_element_clicked(self,space=10,tuple=None) -> WebElement:
        try:
            return WebDriverWait(self.driver, space).until(ec.visibility_of_element_located(tuple))
        except Exception as e:
            print('等待可点击的元素超时，错误{}'.format(e))

if __name__ == '__main__':
    Wait().wait_element_clicked()