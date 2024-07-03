from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class BasePage():

    def __init__(self, driver):
        self.driver = driver


    def get_page(self, url):
        return self.driver.get(url)


    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time, ).until(EC.presence_of_element_located(locator),
                                        message=f"Can't find element by locator {locator}")


    def find_elements(self, locator, time=15):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                         message=f"Can't find elements by locator {locator}")

    def check_title(self, title):
        assert self.driver.title == title


    def check_url(self, url):
        assert self.driver.current_url == url




