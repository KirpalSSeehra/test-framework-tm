from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver


class BasketPage(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    # Select insurance
    def select_insurance(self):
        full_insur = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='tm-insurance-content']/div[2]/div[3]/div[2]/div[5]/fieldset/div/div/div[2]/input")))
        full_insur.click()
        continue_modal = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='tm-insurance-content']/div[3]/div[2]/div[1]")))
        continue_modal.click()

    def change_phone_contract(self):
        change_phone = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#maincontent > div.columns > div.column.main > div.cart-container > div.cart > div > div.active > div:nth-child(2) > div.device-payment > a:nth-child(2)")))
        change_phone.click()

    # Click checkout
    def click_checkout(self):
        check = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div[5]/div[2]/div[2]/ul/li/button")))
        check.click()

