import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_driver import BaseDriver
from selenium.webdriver.support import expected_conditions as EC

from pages.tm_basketpage import BasketPage


# Comment to update GH token again

class ProductDescriptionPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    DEVICE_COLOUR_BTN = "//*[@id='tm-deal-device-wrapper']/div[1]/div/div[1]/div/div[4]"
    DEVICE_STORAGE_BTN = "//span[contains(text(),'256GB')]"
    TARIFF_SELECTOR_BTN = "//*[@id='product-options-wrapper']/div/fieldset[1]/div[4]/div/div[1]/div/div[12]/label"
    ADD_TO_BASKET_BTN = "//*[@id='product-addtocart-button']"
    AB_ADD_TO_BASKET_BTN = "//*[@id='emulate-button-pay-monthly']" #AB = Action Bar
    NEW_CUSTOMER_BTN = "//button[contains(@data-bind, 'click: isNewCustomer')]"
    EXISTING_CUSTOMER_BTN = "//button[contains(@data-bind, 'click: isExistingCustomer')]"
    EXISTING_CUSTOMER_EMAIL_FIELD = "//input[contains(@id, 'customer-email')]"
    EXISTING_CUSTOMER_PW_FIELD = "//input[contains(@id, 'pass')]"
    EXISTING_CUSTOMER_LOGIN_BTN = "//button[@id='send2']"
    ALT_NEW_CUSTOMER_BTN = "//*[@id='button-container-820']/button[3]"
    PAY_MONTHLY_CUSTOMER_BTN = "//*[@id='button-container-820']/button[1]"
    PAY_AS_YOU_GO_CUSTOMER_BTN = "//*[@id='button-container-820']/button[2]"

    def get_device_colour_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEVICE_COLOUR_BTN)

    def select_device_colour_btn(self):
        self.driver.execute_script("arguments[0].click();", self.get_device_colour_btn())

    def get_device_storage_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEVICE_STORAGE_BTN)

    def select_device_storage_btn(self):
        self.driver.execute_script("arguments[0].click();", self.get_device_storage_btn())

    def get_tariff_selector_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.TARIFF_SELECTOR_BTN)

    def select_tariff_selector_btn(self):
        self.driver.execute_script("arguments[0].click();", self.get_tariff_selector_btn())

    def get_add_to_basket_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ADD_TO_BASKET_BTN)

    def select_add_to_basket_btn(self):
        self.driver.execute_script("arguments[0].click();", self.get_add_to_basket_btn())

    def get_ab_add_to_basket_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.AB_ADD_TO_BASKET_BTN)

    def select_ab_add_to_basket_btn(self):
        self.get_ab_add_to_basket_btn().click()

    def get_new_customer_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.NEW_CUSTOMER_BTN)

    def select_new_customer_btn(self):
        self.get_new_customer_btn().click()
        basket_page = BasketPage(self.driver)
        return basket_page

    def get_existing_customer_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EXISTING_CUSTOMER_BTN)

    def select_existing_customer_btn(self):
        self.get_existing_customer_btn().click()

    def get_existing_customer_email_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EXISTING_CUSTOMER_EMAIL_FIELD)

    def enter_existing_customer_email_field(self, customer_email):
        self.get_existing_customer_email_field().send_keys(customer_email)

    def get_existing_customer_pw_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EXISTING_CUSTOMER_PW_FIELD)

    def enter_existing_customer_pw_field(self, customer_pw):
        self.get_existing_customer_pw_field().send_keys(customer_pw)

    def get_existing_customer_login_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EXISTING_CUSTOMER_LOGIN_BTN)

    def select_existing_customer_login_btn(self):
        self.get_existing_customer_login_btn().click()

    def get_alternative_new_customer_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALT_NEW_CUSTOMER_BTN)

    def select_alternative_new_customer_btn(self):
        self.get_alternative_new_customer_btn().click()
        basket_page = BasketPage(self.driver)
        return basket_page

    def get_pay_monthly_customer_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.PAY_MONTHLY_CUSTOMER_BTN)

    def select_pay_monthly_customer_btn(self):
        self.get_pay_monthly_customer_btn().click()
        # basket_page = BasketPage(self.driver)
        # return basket_page

    def get_pay_as_you_go_customer_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.PAY_AS_YOU_GO_CUSTOMER_BTN)

    def select_pay_as_you_go_customer_btn(self):
        self.get_pay_as_you_go_customer_btn().click()
        # basket_page = BasketPage(self.driver)
        # return basket_page

