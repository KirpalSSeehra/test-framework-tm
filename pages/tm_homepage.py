import time

from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from base.base_driver import BaseDriver


class HomePage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    ACCEPT_COOKIES_BTN = "//*[@id='consent_prompt_submit']"
    MANAGE_COOKIES_BTN = "//*[@id='privacy-more-information']"
    MANAGE_EXPERIENCE_BTN = "//label[contains(@for, 'toggle_cat1')]"
    MANAGE_ADVERTISING_BTN = "//label[contains(@for, 'toggle_cat2')]"
    MANAGE_SAVE_PREFERENCES_BTN = "//*[@id='preferences_prompt_submit']"
    SEARCH_BAR_FIELD = "search"


    def getAcceptCookiesBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ACCEPT_COOKIES_BTN)

    def getManageCookiesBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.MANAGE_COOKIES_BTN)

    def getManageExperienceBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.MANAGE_EXPERIENCE_BTN)

    def getManageAdvertisingBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.MANAGE_ADVERTISING_BTN)

    def getManageSavePreferencesBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.MANAGE_SAVE_PREFERENCES_BTN)

    def getSearchBarField(self):
        return self.wait_until_element_is_clickable(By.ID, self.SEARCH_BAR_FIELD)

    def selectAcceptCookiesBtn(self):
        self.getAcceptCookiesBtn().click()

    def selectManageCookiesBtn(self):
        self.getManageCookiesBtn().click()

    def selectManageExperienceBtn(self):
        self.getManageExperienceBtn().click()

    def selectManageAdvertisingBtn(self):
        self.getManageAdvertisingBtn().click()

    def selectManageSavePreferencesBtn(self):
        self.getManageSavePreferencesBtn().click()

    def enterSearchBarField(self, searchbar):
        self.getSearchBarField().send_keys(searchbar)
        self.getSearchBarField().send_keys(Keys.ENTER)


