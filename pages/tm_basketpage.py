from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class BasketPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Select insurance
    def select_full_insurance(self):
        full_insur = self.wait_until_element_is_clickable(By.XPATH, "//*[@id='tm-insurance-content']/div[2]/div[3]/div[2]/div[5]/fieldset/div/div/div[2]/input")
        full_insur.click()

        # Option to select back button on insurance modal
        # back_btn = self.wait_until_element_is_clickable(By.XPATH, "//*[@id='tm-insurance-content']/div[3]/div[2]/div[2]")
        # back_btn.click()

        continue_btn = self.wait_until_element_is_clickable(By.XPATH, "//*[@id='tm-insurance-content']/div[3]/div[2]/div[1]")
        continue_btn.click()

    # Select change device contract button
    def change_phone_contract(self):
        change_phone = self.wait_until_element_is_clickable(By.XPATH, "//*[@id='maincontent']/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[1]/a[2]")
        change_phone.click()

    # Select change safety buffer button
    def change_safety_buffer(self):
        change_safety = self.wait_until_element_is_clickable(By.XPATH, "//*[@id='maincontent']/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/a")
        change_safety.click()

    # Select change insurance button
    def change_insurance(self):
        change_insurance = self.wait_until_element_is_clickable(By.XPATH, "//*[@id='maincontent']/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/a")
        change_insurance.click()

    # Click checkout
    def click_checkout(self):
        check = self.wait_until_element_is_clickable(By.XPATH, "//button[@title='Go to checkout']")
        check.click()