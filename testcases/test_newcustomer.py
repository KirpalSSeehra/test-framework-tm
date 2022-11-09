import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.tm_homepage import HomePage
from pages.tm_catalogue_search import CatalogueSearch


@pytest.mark.usefixtures("setup")
class TestNewCustomer():
    def test_purchase_device(self):

        hp = HomePage(self.driver, self.wait)
        cs = CatalogueSearch(self.driver, self.wait)

        # Accept cookies
        hp.click_cookies()
        # Search for device
        hp.search_device("iphone 14")

        # Select first carousel item
        cs.select_device()

        # Add to basket
        add_basket = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='emulate-button-pay-monthly']")))
        add_basket.click()
        time.sleep(6)
        #
        # New customer button click
        new_cust = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-bind, 'click: isNewCustomer')]")))
        new_cust.click()
        time.sleep(8)
        #
        # Full insurance click and continue modal
        full_insur = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tm-insurance-content']/div[2]/div[3]/div[2]/div[5]/fieldset/div/div/div[2]/input")))
        full_insur.click()
        continue_modal = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tm-insurance-content']/div[3]/div[2]/div[1]")))
        continue_modal.click()
        #
        # # checkout button
        check = self.wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/main/div[5]/div[2]/div[2]/ul/li/button")))
        check.click()
        time.sleep(8)

