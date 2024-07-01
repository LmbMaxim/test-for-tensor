import os
import pytest
from selenium import webdriver



@pytest.fixture(scope='session')
def driver():

    options = webdriver.ChromeOptions() ;
    path = os.getcwd()
    prefs = {"download.default_directory" : path}
    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()






