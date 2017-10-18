# -*- coding:UTF-8 -*-
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.remote.webdriver import WebDriver
import time


class Demo:
    def __init__(self):
        pass

    @staticmethod
    def get_current_web_driver():
        return BuiltIn().get_library_instance(u"Selenium2Library")._current_browser()

    @staticmethod
    def do_something():
        """
        Do something.
        :return:
        """
        driver = Demo.get_current_web_driver()
        if isinstance(driver, WebDriver) and driver is not None:
            driver.find_element_by_id("kw").send_keys("Test")
            time.sleep(2)
        else:
            raise Exception(u"浏览器没有启动！")
