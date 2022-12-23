import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_email_address(self, emailadd):
        enter_email = self.wait_until_element_is_clickable(By.XPATH, "//*[@id='customer-email']")
        enter_email.send_keys(emailadd)

    def confirm_email_address(self, confirmemail):
        confirm_email = self.wait_until_element_is_clickable(By.XPATH, "//*[@id='customer-confirm-email']")
        confirm_email.send_keys(confirmemail)

    def select_title(self):
        wait = WebDriverWait(self.driver, 20)
        title = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@name, 'ko_unique_4')]")))
        self.driver.execute_script("arguments[0].click();", title)

    def enter_firstname(self, fn):
        first_name = self.wait_until_element_is_clickable(By.NAME, "customer[firstname]")
        first_name.send_keys(fn)

    def enter_lastname(self, ln):
        last_name = self.wait_until_element_is_clickable(By.NAME, "customer[lastname]")
        last_name.send_keys(ln)

    def enter_dob(self, dd, mm, yyyy):
        enter_day = self.wait_until_element_is_clickable(By.ID, "customer-day")
        enter_day.send_keys(dd)
        enter_month = self.wait_until_element_is_clickable(By.ID, "customer-month")
        enter_month.send_keys(mm)
        enter_year = self.wait_until_element_is_clickable(By.ID, "customer-year")
        enter_year.send_keys(yyyy)


    def select_type_of_account(self):
        wait = WebDriverWait(self.driver, 20)
        select_account_type = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@name, 'ko_unique_6')]")))
        self.driver.execute_script("arguments[0].click();", select_account_type)

    def enter_contact_number(self, contactno):
        contact_number = self.wait_until_element_is_clickable(By.NAME, "customer[tm_contact_number]")
        contact_number.send_keys(contactno)

    def enter_address(self, currentaddress, currentpostcode):
        curr_address1 = self.wait_until_element_is_clickable(By.NAME, "billing_address[tm_building_id]")
        curr_address1.send_keys(currentaddress)
        curr_post = self.wait_until_element_is_clickable(By.NAME, "billing_address[postcode]")
        curr_post.send_keys(currentpostcode)


    def find_current_address(self):
        find_add = self.wait_until_element_is_clickable(By.XPATH, "//a[contains(@data-bind, 'click: findAddress')]")
        find_add.click()

    def enter_address_date(self, mm, yyyy):
        address_month = self.wait_until_element_is_clickable(By.NAME, "billing_address[tm_start_date][month]")
        address_month.send_keys(mm)
        address_year = self.wait_until_element_is_clickable(By.NAME, "billing_address[tm_start_date][year]")
        address_year.send_keys(yyyy)
        address_year.send_keys(Keys.ENTER)

    def enter_previous_address(self, previousaddress, prevpostcode):
        prev_address1 = self.wait_until_element_is_clickable(By.NAME, "previous_address[tm_building_id]")
        prev_address1.send_keys(previousaddress)
        prev_post = self.wait_until_element_is_clickable(By.NAME, "previous_address[postcode]")
        prev_post.send_keys(prevpostcode)

    def find_previous_address(self):
        find_prev_address = self.wait_until_element_is_clickable(By.XPATH, "//*[@id='about-form']/fieldset[2]/div[4]/a")
        find_prev_address.click()

    def enter_previous_address_date(self, prevmm, prevyyyy):
        prev_address_month = self.wait_until_element_is_clickable(By.NAME, "previous_address[tm_start_date][month]")
        prev_address_month.send_keys(prevmm)
        prev_address_year = self.wait_until_element_is_clickable(By.NAME, "previous_address[tm_start_date][year]")
        prev_address_year.send_keys(prevyyyy)
        prev_address_year.send_keys(Keys.ENTER)

    def create_account_pw(self, pw, confirmpw):
        create_pw = self.wait_until_element_is_clickable(By.ID, "customer-password")
        create_pw.send_keys(pw)
        confirm_pw = self.wait_until_element_is_clickable(By.ID, "customer-confirm-password")
        confirm_pw.send_keys(confirmpw)
        show_hide_pw = self.wait_until_element_is_clickable(By.XPATH,"//a[contains(@data-bind, 'click: showHidePassword')]")
        show_hide_pw.click()


    def select_security_question(self):
        security_question = self.wait_until_element_is_clickable(By.XPATH, "//select[@name='account[tm_security_question]']")
        sq = Select(security_question)
        sq.select_by_visible_text("Your town/city of birth?")

    def enter_security_question(self, securityanswer):

        security_answer = self.wait_until_element_is_clickable(By.NAME, "account[tm_security_answer]")
        security_answer.send_keys(securityanswer)
        show_hide_answer = self.wait_until_element_is_clickable(By.XPATH, "//a[contains(@data-bind, 'click: showHideAnswer')]")
        show_hide_answer.click()










