from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage



class TensorHomeLocators:

    LOCATOR_COOKIE = (By.CLASS_NAME, 'tensor_ru-CookieAgreement__close')
    LOCATOR_STR_IN_PEOPLE = (By.CLASS_NAME, 'tensor_ru-Index__block4-content ')
    LOCATOR_STR_IN_PEOPLE_DETAILS = (By.XPATH, """//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]
                                                  /div/p[4]/a""")


class TensorHome(BasePage):

    URL = 'https://tensor.ru/'

    def get_tensor_page(self):
        return self.get_page(self.URL)


    def strength_in_people_banner(self):
        assert self.find_element(TensorHomeLocators.LOCATOR_STR_IN_PEOPLE)
        return 0


    def click_strength_in_people_details(self):
        elements = self.find_element(TensorHomeLocators.LOCATOR_STR_IN_PEOPLE_DETAILS).click()
        return 0


    def check_tensor_home_title(self):
        assert self.driver.title == 'Тензор — IT-компания'
        return 0


    def check_tensor_about_url(self):
        print(self.driver.title)
        assert self.driver.current_url  == 'https://tensor.ru/about'
        return 0


    def close_cookie_msg(self):
        self.find_element(TensorHomeLocators.LOCATOR_COOKIE).click()
