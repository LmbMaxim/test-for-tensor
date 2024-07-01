from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from page_objects.base_page import BasePage



class SbisContactsLocators:

    LOCATOR_TENSOR_BANER = (By.CLASS_NAME, 'sbisru-Contacts__logo-tensor')
    LOCATOR_REGION_NAME = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text.sbis_ru-link')
    LOACTOR_PARTNERS_LIST = (By.CLASS_NAME, 'sbisru-Contacts-List__col.ws-flex-shrink-1.ws-flex-grow-1')


class NewRegionLocators:

    LOCATOR_NEW_REGION = (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span')
    LOCATOR_NEW_REGION_LIST = (By.XPATH, 'sbis_ru-Region-Chooser__text sbis_ru-link')


class SbisContacts(BasePage):

    URL = 'https://sbis.ru/contacts'
    REGION = 'Нижегородская обл.'
    EXPECTED_TITLE_KK = 'СБИС Контакты — Камчатский край'

    def get_sbis_contacts_page(self):
        return self.get_page(self.URL)


    def click_banner_tensor(self):
        return self.find_element(SbisContactsLocators.LOCATOR_TENSOR_BANER).click()


    def check_region(self, region=REGION):
        assert region == self.find_element(SbisContactsLocators.LOCATOR_REGION_NAME).text
        return 0


    def check_partners_list(self):
        assert self.find_element(SbisContactsLocators.LOACTOR_PARTNERS_LIST)
        return 0


    def set_new_region(self):
        region = self.find_element(SbisContactsLocators.LOCATOR_REGION_NAME).click()
        self.find_element(NewRegionLocators.LOCATOR_NEW_REGION).click()
        return 0


    def check_new_region(self):
        self.check_region('Камчатский край')


    def check_new_title(self):
        self.check_title(self.EXPECTED_TITLE_KK)


    def check_new_url(self):
        self.check_url('https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients')



