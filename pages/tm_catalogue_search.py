from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver


class CatalogueSearch(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    # Select first carousel item
    def select_device(self):
        selectdevice = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='instant-search-results-container']/div/div/ol/li[1]/div/div/a")))
        selectdevice.click()

