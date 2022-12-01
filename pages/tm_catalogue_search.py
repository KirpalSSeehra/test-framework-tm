from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class CatalogueSearch(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Select first carousel item
    def select_device(self):
        select_dev = self.wait_until_element_is_clickable(By.XPATH, "//*[@id='instant-search-results-container']/div/div/ol/li[1]/div/div/a")
        # Can use below XPath to select next list element for Iphone 12
        # select_dev = self.wait_until_element_is_clickable(By.XPATH, "//*[@id='instant-search-results-container']/div/div/ol/li[2]/div/div/a")
        select_dev.click()

