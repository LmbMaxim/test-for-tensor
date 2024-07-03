import time

from page_objects.sbis_contacts import SbisContacts



def tests_at_sbis_contacts_page(driver):
    sbis_contacts = SbisContacts(driver)
    sbis_contacts.get_sbis_contacts_page()
    sbis_contacts.check_region()
    sbis_contacts.check_partners_list()

    sbis_contacts.set_new_region()
    time.sleep(2)

    sbis_contacts.check_new_region()
    sbis_contacts.check_new_title()
    sbis_contacts.check_new_url()
    sbis_contacts.check_partners_list()
    
    
    
