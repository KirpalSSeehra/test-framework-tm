import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_driver import BaseDriver
from selenium.webdriver.support import expected_conditions as EC

# Comment to update GH token

class ProductDescriptionPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    DEVICE_COLOUR_BTN = "//*[@id='tm-deal-device-wrapper']/div[1]/div/div[1]/div/div[4]"
    DEVICE_STORAGE_BTN = "//span[contains(text(),'256GB')]"
    TARIFF_SELECTOR_BTN = "//*[@id='bundle-option-14701-40651']"
    ADD_TO_BASKET_BTN = "//*[@id='product-addtocart-button']"
    AB_ADD_TO_BASKET_BTN = "//*[@id='emulate-button-pay-monthly']" #AB = Action Bar
    NEW_CUSTOMER_BTN = "//button[contains(@data-bind, 'click: isNewCustomer')]"
    EXISTING_CUSTOMER_BTN = "//button[contains(@data-bind, 'click: isExistingCustomer')]"
    EXISTING_CUSTOMER_EMAIL_FIELD = "//input[contains(@id, 'customer-email')]"
    EXISTING_CUSTOMER_PW_FIELD = "//input[contains(@id, 'pass')]"
    EXISTING_CUSTOMER_LOGIN_BTN = "//button[@id='send2']"

    def getDeviceColourBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEVICE_COLOUR_BTN)

    def selectDeviceColourBtn(self):
        self.driver.execute_script("arguments[0].click();", self.getDeviceColourBtn())

    def getDeviceStorageBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEVICE_STORAGE_BTN)

    def selectDeviceStorageBtn(self):
        self.driver.execute_script("arguments[0].click();", self.getDeviceStorageBtn())

    def getTariffSelectorBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.TARIFF_SELECTOR_BTN)

    def selectTariffSelectorBtn(self):
        self.driver.execute_script("arguments[0].click();", self.getTariffSelectorBtn())

    def getAddToBasketBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ADD_TO_BASKET_BTN)

    def selectAddToBasketBtn(self):
        self.driver.execute_script("arguments[0].click();", self.getAddToBasketBtn())

    def getAbAddToBasketBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.AB_ADD_TO_BASKET_BTN)

    def selectAbAddToBasketBtn(self):
        self.getAbAddToBasketBtn().click()

    def getNewCustomerBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.NEW_CUSTOMER_BTN)

    def selectNewCustomerBtn(self):
        self.getNewCustomerBtn().click()

    def getExistingCustomerBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EXISTING_CUSTOMER_BTN)

    def selectExistingCustomerBtn(self):
        self.getExistingCustomerBtn().click()

    def getExistingCustomerEmailField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EXISTING_CUSTOMER_EMAIL_FIELD)

    def enterExistingCustomerEmailField(self, customer_email):
        self.getExistingCustomerEmailField().send_keys(customer_email)

    def getExistingCustomerPwField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EXISTING_CUSTOMER_PW_FIELD)

    def enterExistingCustomerPwField(self, customer_pw):
        self.getExistingCustomerPwField().send_keys(customer_pw)

    def getExistingCustomerLoginBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EXISTING_CUSTOMER_LOGIN_BTN)

    def selectExistingCustomerLoginBtn(self):
        self.getExistingCustomerLoginBtn().click()




