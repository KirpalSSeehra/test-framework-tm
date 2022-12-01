import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver


class ProductDescriptionPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_device_colour(self):
        select_colour = self.wait_until_element_is_clickable(By.XPATH, "//span[contains(text(), 'Purple')]")
        select_colour.click()

    def select_device_storage(self):
        select_storage = self.wait_until_element_is_clickable(By.XPATH, "//span[contains(text(),'256GB')]")
        select_storage.click()

    def click_add_to_basket(self):
        add_basket = self.wait_until_element_is_clickable(By.XPATH, "//*[@id='emulate-button-pay-monthly']")
        add_basket.click()

    def select_new_customer(self):
        new_cust = self.wait_until_element_is_clickable(By.XPATH, "//button[contains(@data-bind, 'click: isNewCustomer')]")
        new_cust.click()

    def select_existing_customer(self):
        existing_cust = self.wait_until_element_is_clickable(By.XPATH, "//button[contains(@data-bind, 'click: isExistingCustomer')]")
        existing_cust.click()

    def enter_existing_customer_details(self, cust_email, cust_pw):
        existing_cust_email = self.wait_until_element_is_clickable(By.XPATH, "//input[contains(@id, 'customer-email')]")
        existing_cust_email.send_keys(cust_email)
        time.sleep(2)
        existing_cust_pw = self.wait_until_element_is_clickable(By.XPATH, "//input[contains(@id, 'pass')]")
        existing_cust_pw.send_keys(cust_pw)
        time.sleep(2)
        existing_cust_login = self.wait_until_element_is_clickable(By.XPATH, "//Button[@id='send2']")
        existing_cust_login.click()
        time.sleep(2)




