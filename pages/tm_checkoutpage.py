import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver


class CheckoutPage(BaseDriver):

    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    def enter_email_address(self, emailadd):
        enter_email = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='customer-email']")))
        enter_email.send_keys(emailadd)

    def confirm_email_address(self, confirmemail):
        confirm_email = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='customer-confirm-email']")))
        confirm_email.send_keys(confirmemail)

    def select_title(self):
        title = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div[3]/div/div/div[3]/ol/li[1]/div[2]/form/div[1]/div[2]/div/fieldset/div/div[3]/label")))
        title.click()

    def enter_firstname(self, fn):
        first_name = self.wait.until(EC.element_to_be_clickable((By.NAME, "customer[firstname]")))
        first_name.send_keys(fn)

    def enter_lastname(self, ln):
        last_name = self.wait.until(EC.element_to_be_clickable((By.NAME, "customer[lastname]")))
        last_name.send_keys(ln)

    def enter_dob(self, dd, mm, yyyy):
        enter_day = self.wait.until(EC.element_to_be_clickable((By.ID, "customer-day")))
        enter_day.send_keys(dd)
        enter_month = self.wait.until(EC.element_to_be_clickable((By.ID, "customer-month")))
        enter_month.send_keys(mm)
        enter_year = self.wait.until(EC.element_to_be_clickable((By.ID, "customer-year")))
        enter_year.send_keys(yyyy)

    def check_type_of_account_selected(self):
        check_account = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#about-form > div:nth-child(9) > div > fieldset > div > div:nth-child(2) > label")))
        print(check_account.is_selected())

    def select_type_of_account(self):
        select_account = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div//label[contains(text(), 'Business')]")))
        select_account.click()

    def enter_contact_number(self, contactno):
        contact_number = self.wait.until(EC.element_to_be_clickable((By.NAME, "customer[tm_contact_number]")))
        contact_number.send_keys(contactno)

    def enter_address(self, addressline1, postcode):
        address1 = self.wait.until(EC.element_to_be_clickable((By.NAME, "billing_address[tm_building_id]")))
        address1.send_keys(addressline1)
        post = self.wait.until(EC.element_to_be_clickable((By.NAME, "billing_address[postcode]")))
        post.send_keys(postcode)


    def find_address(self):
        findadd = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@data-bind, 'click: findAddress')]")))
        findadd.click()


