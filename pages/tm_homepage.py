import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC


class HomePage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Accept cookies
    def click_cookies(self):
        clickcookies = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Accept all cookies']")))
        clickcookies.click()

    # Search for iphone
    def search_device(self, searchDevice):
        searchdevice = self.wait.until(EC.element_to_be_clickable((By.ID, "search")))
        searchdevice.send_keys(searchDevice)
        searchdevice.send_keys(Keys.ENTER)


