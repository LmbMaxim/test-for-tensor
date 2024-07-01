import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_objects.sbis_home import SbisHome
from page_objects.sbis_contacts import SbisContacts
from page_objects.tensor_home import TensorHome
from page_objects.tensor_about import TensorAbout



def tests_on_sbis_contacts(driver):

    sbis_contacts = SbisContacts(driver)
    sbis_contacts.get_sbis_contacts_page()
    sbis_contacts.click_banner_tensor()
    
    #Swith to the first tab after open a new tab.So selenium can interact with the next page.
    windows = driver.window_handles
    driver.switch_to.window(windows[0])


def tests_on_tensor_home(driver):

    tensor_home = TensorHome(driver)
    tensor_home.get_tensor_page()
    tensor_home.strength_in_people_banner()

    tensor_home.close_cookie_msg()
    tensor_home.click_strength_in_people_details()
    tensor_home.check_tensor_about_url()


def tests_on_tensor_about(driver):
    tensor_about = TensorAbout(driver)
    tensor_about.get_tensor_about_page()
    tensor_about.get_we_are_working_gallery()
    
