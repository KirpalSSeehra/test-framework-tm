import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver


class CheckoutPage(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    def enter_email_address(self):
        enter_email = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='customer-email']")))
        enter_email.send_keys("kirpal-seehra@hotmail.co.uk")

    def confirm_email_address(self):
        confirm_email = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='customer-confirm-email']")))
        confirm_email.send_keys("kirpal-seehra@hotmail.co.uk")

    def select_title(self):
        title = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div[3]/ol/li[1]/div[2]/form/div[1]/div[2]/div/fieldset/div/div[3]/label")))
        title.click()

    def enter_firstname(self):
        first_name = self.wait.until(EC.element_to_be_clickable((By.NAME, "customer[firstname]")))
        first_name.send_keys("Kirpal")

    def enter_lastname(self):
        last_name = self.wait.until(EC.element_to_be_clickable((By.NAME, "customer[lastname]")))
        last_name.send_keys("Seehra")

    def enter_dob(self):
        enter_day = self.wait.until(EC.element_to_be_clickable((By.ID, "customer-day")))
        enter_day.send_keys("03")
        enter_month = self.wait.until(EC.element_to_be_clickable((By.ID, "customer-month")))
        enter_month.send_keys("10")
        enter_year = self.wait.until(EC.element_to_be_clickable((By.ID, "customer-year")))
        enter_year.send_keys("1994")

    def check_type_of_account_selected(self):
        check_account = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#about-form > div:nth-child(9) > div > fieldset > div > div:nth-child(2) > label")))
        print(check_account.is_selected())

    def select_type_of_account(self):
        select_account = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='6']"))).click()

    def enter_contact_number(self):
        contact_number = self.wait.until(EC.element_to_be_clickable((By.NAME, "customer[tm_contact_number]")))
        contact_number.send_keys("07940490912")
