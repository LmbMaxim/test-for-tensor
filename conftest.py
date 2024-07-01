import pytest
from selenium import webdriver



@pytest.fixture(scope='session')
def driver():

    options = webdriver.ChromeOptions() ;
    prefs = {"download.default_directory" : "/home/maxim/src/for-tensor/"}
    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()






