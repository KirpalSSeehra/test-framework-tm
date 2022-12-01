import time

from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from base.base_driver import BaseDriver


class HomePage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Accept cookies
    def accept_cookies(self):
        accept_cookie = self.wait_until_element_is_clickable(By.XPATH, "//*[@id='consent_prompt_submit']")
        accept_cookie.click()


    # Manage cookies
    def manage_cookies(self):
        manage_cookie = self.wait_until_element_is_clickable(By.XPATH,"//*[@id='privacy-more-information']")
        manage_cookie.click()
        experience_toggle = self.wait_until_element_is_clickable(By.XPATH, "//label[contains(@for, 'toggle_cat1')]")
        experience_toggle.click()
        time.sleep(2)
        advertising_toggle = self.wait_until_element_is_clickable(By.XPATH, "//label[contains(@for, 'toggle_cat2')]")
        advertising_toggle.click()
        time.sleep(2)
        save_preferences = self.wait_until_element_is_clickable(By.XPATH, "//*[@id='preferences_prompt_submit']")
        save_preferences.click()
        time.sleep(2)

    # Search for iphone
    def search_device(self, searchdevice):
        search_dev = self.wait_until_element_is_clickable(By.ID, "search")
        search_dev.send_keys(searchdevice)
        search_dev.send_keys(Keys.ENTER)


