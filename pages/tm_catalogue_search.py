from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class CatalogueSearch(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # "//*[@id='instant-search-results-container']/div/div/ol/li[2]/div/div/a") to select next item in list.
    # Need to create a loop here to cycle through items.
    # Select first carousel item

    # Locators
    SELECT_DEVICE_ITEM = "//*[@id='instant-search-results-container']/div/div/ol/li[1]/div/div/a"

    def getDeviceItem(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DEVICE_ITEM)

    def selectDeviceItem(self):
        self.getDeviceItem().click()
