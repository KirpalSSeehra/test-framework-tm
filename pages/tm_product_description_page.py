from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver


class ProductDescriptionPage(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    # def select_device_colour(self):
    #     select_colour = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tm-deal-device-wrapper']/div[1]/div/div[1]/div")))
    #     select_colour.click()

    # def select_device_storage(self):
    #     select_storage = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tm-deal-device-wrapper']/div[1]/div/div[2]/div/div[2]")))
    #     select_storage.click()

    def click_add_to_basket(self):
        add_basket = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='emulate-button-pay-monthly']")))
        add_basket.click()

    def select_type_of_customer(self):
        new_cust = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-bind, 'click: isNewCustomer')]")))
        new_cust.click()