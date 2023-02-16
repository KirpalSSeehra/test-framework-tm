import time

from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from base.base_driver import BaseDriver
from pages.tm_catalogue_search import CatalogueSearch


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

    def get_accept_cookies_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ACCEPT_COOKIES_BTN)

    def get_manage_cookies_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.MANAGE_COOKIES_BTN)

    def get_manage_experience_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.MANAGE_EXPERIENCE_BTN)

    def get_manage_advertising_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.MANAGE_ADVERTISING_BTN)

    def get_manage_save_preferences_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.MANAGE_SAVE_PREFERENCES_BTN)

    def get_search_bar_field(self):
        return self.wait_until_element_is_clickable(By.ID, self.SEARCH_BAR_FIELD)

    def select_accept_cookies_btn(self):
        self.get_accept_cookies_btn().click()

    def select_manage_cookies_btn(self):
        self.get_manage_cookies_btn().click()

    def select_manage_experience_btn(self):
        self.get_manage_experience_btn().click()

    def select_manage_advertising_btn(self):
        self.get_manage_advertising_btn().click()

    def select_manage_save_preferences_btn(self):
        self.get_manage_save_preferences_btn().click()

    def enter_search_bar_field(self, searchbar):
        self.get_search_bar_field().send_keys(searchbar)
        self.get_search_bar_field().send_keys(Keys.ENTER)
        catalogue_search = CatalogueSearch(self.driver)
        return catalogue_search


