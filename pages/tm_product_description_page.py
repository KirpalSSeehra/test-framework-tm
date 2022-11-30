from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver


class ProductDescriptionPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait

    def select_device_colour(self):
        # select_colour = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Purple')]")))
        select_colour = self.wait_until_element_is_clickable(By.XPATH, "//span[contains(text(), 'Purple')]")
        select_colour.click()

    def select_device_storage(self):
        # select_storage = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'256GB')]")))
        select_storage = self.wait_until_element_is_clickable(By.XPATH, "//span[contains(text(),'256GB')]")
        select_storage.click()

    def click_add_to_basket(self):
        # add_basket = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='emulate-button-pay-monthly']")))
        add_basket = self.wait_until_element_is_clickable(By.XPATH, "//*[@id='emulate-button-pay-monthly']")
        add_basket.click()

    def select_type_of_customer(self):
        # new_cust = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-bind, 'click: isNewCustomer')]")))
        new_cust = self.wait_until_element_is_clickable(By.XPATH, "//button[contains(@data-bind, 'click: isNewCustomer')]")
        new_cust.click()