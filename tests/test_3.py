import time

from page_objects.sbis_home import SbisHome
from page_objects.sbis_contacts import SbisContacts
from page_objects.sbis_downloads import SbisDownloads


def test_download_local_versions_(driver):
    sbis_home = SbisHome(driver)
    sbis_home.get_sbis_home()

    sbis_home.close_cooke_msg()

    #Get url to download page from home page
    url = sbis_home.get_download_local_versions_link()
    
    #Get download page with url from home page
    sbis_downloads = SbisDownloads(driver)
    sbis_downloads.get_page(url)
    sbis_downloads.download_web_installer()

    time.sleep(8)
    sbis_downloads.plugin_size_accurate()
    sbis_downloads.remove_plugin_file()



