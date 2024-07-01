import os
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By



class SbisDownloadsLocators:

    LOCATOR_WEB_INSTALLER = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/a')


class SbisDownloads(BasePage):

    def download_web_installer(self):
        self.find_element(SbisDownloadsLocators.LOCATOR_WEB_INSTALLER).click()

    
    def GetHumanReadable(self, size,precision=2):
        # suffixes=['B','KB','MB','GB','TB']
        suffixIndex = 0
        while size > 1024 and suffixIndex < 4:
            suffixIndex += 1 #increment the index of the suffix
            size = size/1024.0 #apply the division
        # return "%.*f%s"%(precision,size,suffixes[suffixIndex])
        return "%.*f"%(precision,size)


    def get_expected_plugin_size(self):
        link_text = self.find_element(SbisDownloadsLocators.LOCATOR_WEB_INSTALLER).text
        expected_size = link_text.split()[2]
        return expected_size


    def get_real_plugin_size(self):
        s = os.path.getsize('sbisplugin-setup-web.exe')
        size = self.GetHumanReadable(s)
        return size


    def plugin_size_accurate(self):
        assert self.get_real_plugin_size() == self.get_expected_plugin_size()


    def remove_plugin_file(self):
        os.remove('sbisplugin-setup-web.exe')
