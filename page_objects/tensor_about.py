from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By



class TensorAboutLocators:

    LOCATOR_WE_ARE_WORKING_GALLARY = (By.CSS_SELECTOR, ".tensor_ru-About__block3-image-wrapper > img")


class TensorAbout(BasePage):

    url = 'https://tensor.ru/about'

    def get_tensor_about_page(self):
        return self.get_page(self.url)


    def get_we_are_working_gallery(self):
        # Collect width and height pairs of each image in to list.
        # set() this list
        # If leanth of set is 2, size of all images are equal.

        elems = list(self.find_elements(TensorAboutLocators.LOCATOR_WE_ARE_WORKING_GALLARY))
        pairs_list = []
        for i in elems:
            w = i.get_attribute('width')
            h = i.get_attribute('height')
            pairs_list.append((w, h))

        assert(len(set(pairs_list))) != 2
        return 0
        
        
            

