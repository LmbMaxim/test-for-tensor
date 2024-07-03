from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class SbisHomeLocators:

    LOCATOR_CONTACTS_LINK = (By.LINK_TEXT, 'Контакты')
    LOCATOR_BANNER_TENSOR = (By.CLASS_NAME, 'sbisru-Header__menu-link')
    LOCATOR_DOWNLOADS = (By.LINK_TEXT, 'Скачать локальные версии')
    LOCATOR_CLOSE_COOKIE = (By.CLASS_NAME, 'sbis_ru-CookieAgreement__close')


class SbisHome(BasePage):

    URL = 'https://sbis.ru/'
    # title_home = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
    # title_contact = 'СБИС Контакты — Нижегородская область'

    def get_sbis_home(self):
        return self.get_page(self.URL)


    def click_contacts(self):
        return self.find_element(SbisHomeLocators.LOCATOR_CONTACTS_LINK).click()


    def close_cooke_msg(self):
        return self.find_element(SbisHomeLocators.LOCATOR_CLOSE_COOKIE).click()


    def get_download_local_versions_link(self):
        return self.find_element(SbisHomeLocators.LOCATOR_DOWNLOADS).get_attribute('href')

    




