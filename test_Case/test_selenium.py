import time

from  selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestSelenium():
    def setup(self):
        self.driver=webdriver.Chrome(executable_path='driver path')
        # 浏览器最大化
        self.driver.maximize_window()
        # 隐式等待：动态等待5秒，5秒后仍未响应就报错
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    def test_selenium(self):

        self.driver.get("https://www.huobi.be/zh-cn/exchange/?src=https%3A%2F%2Ffutures.huobi.be&inviter_id=11314840")
        # sleep(2)
        self.driver.find_element(By.NAME,"行情").click()
        # sleep(2)
        self.driver.find_element(By.NAME,"自选").click()
        # sleep(2)
