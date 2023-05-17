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

    # Locators
    EMAIL_ADDRESS_FIELD = "//*[@id='customer-email']"
    CONFIRM_EMAIL_ADDRESS_FIELD = "//*[@id='customer-confirm-email']"
    # SELECT_TITLE_BTN = ""
    FIRST_NAME_FIELD = "customer[firstname]"
    LAST_NAME_FIELD = "customer[lastname]"
    DOB_DATE_FIELD = "customer[dob][day]"
    DOB_MONTH_FIELD = "customer[dob][month]"
    DOB_YEAR_FIELD = "customer[dob][year]"
    # SELECT_ACCOUNT_TYPE_BTN
    CONTACT_NO_FIELD = "customer[tm_contact_number]"
    CURRENT_ADDRESS_LINE_FIELD = "billing_address[tm_building_id]"
    CURRENT_POSTCODE_FIELD = "billing_address[postcode]"
    FIND_CURRENT_ADDRESS_BTN = "//a[contains(@data-bind, 'click: findAddress')]"
    CURRENT_ADDRESS_MONTH_FIELD = "billing_address[tm_start_date][month]"
    CURRENT_ADDRESS_YEAR_FIELD = "billing_address[tm_start_date][year]"
    PREVIOUS_ADDRESS_LINE_FIELD = "previous_address[tm_building_id]"
    PREVIOUS_POSTCODE_FIELD = "previous_address[postcode]"
    FIND_PREVIOUS_ADDRESS_BTN = "//*[@id='about-form']/fieldset[3]/div[4]"
    PREVIOUS_ADDRESS_MONTH_FIELD = "previous_address[tm_start_date][month]"
    PREVIOUS_ADDRESS_YEAR_FIELD = "previous_address[tm_start_date][year]"
    CREATE_PW_FIELD = "customer-password"
    CONFIRM_PW_FIELD = "customer-confirm-password"
    SHOW_HIDE_PW_BTN = "//a[contains(@data-bind, 'click: showHidePassword')]"
    SECURITY_QUESTION_DROPDOWN = "//select[@name='account[tm_security_question]']"
    SECURITY_ANSWER_FIELD = "account[tm_security_answer]"
    SECURITY_ANSWER_SHOW_HIDE_BTN = "//a[contains(@data-bind, 'click: showHideAnswer')]"
    CLUBCARD_NUMBER_FIELD = "tm_clubcard_number"
    TERMS_CONDITIONS_AGREEMENT_CHECKBOX = "//*[@id='agreement_3']"
    ABOUT_YOU_CONFIRM_BTN = "//*[@id='about-buttons-container']/div/button"

    # Get Methods
    def get_email_address_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EMAIL_ADDRESS_FIELD)

    def get_confirm_email_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CONFIRM_EMAIL_ADDRESS_FIELD)

    def get_first_name_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.FIRST_NAME_FIELD)

    def get_last_name_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.LAST_NAME_FIELD)

    def get_dob_date_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.DOB_DATE_FIELD)

    def get_dob_month_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.DOB_MONTH_FIELD)

    def get_dob_year_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.DOB_YEAR_FIELD)

    def get_contact_number_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.CONTACT_NO_FIELD)

    def get_current_address_line_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.CURRENT_ADDRESS_LINE_FIELD)

    def get_current_address_postcode_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.CURRENT_POSTCODE_FIELD)

    def get_find_current_address_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FIND_CURRENT_ADDRESS_BTN)

    def get_current_address_month_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.CURRENT_ADDRESS_MONTH_FIELD)

    def get_current_address_year_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.CURRENT_ADDRESS_YEAR_FIELD)

    def get_previous_address_line_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.PREVIOUS_ADDRESS_LINE_FIELD)

    def get_previous_address_postcode_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.PREVIOUS_POSTCODE_FIELD)

    def get_previous_find_address_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FIND_PREVIOUS_ADDRESS_BTN)

    def get_previous_address_month_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.PREVIOUS_ADDRESS_MONTH_FIELD)

    def get_previous_address_year_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.PREVIOUS_ADDRESS_YEAR_FIELD)

    def get_create_pw_field(self):
        return self.wait_until_element_is_clickable(By.ID, self.CREATE_PW_FIELD)

    def get_confirm_pw_field(self):
        return self.wait_until_element_is_clickable(By.ID, self.CONFIRM_PW_FIELD)

    def get_show_hide_pw_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SHOW_HIDE_PW_BTN)

    def get_security_question_dropdown(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SECURITY_QUESTION_DROPDOWN)

    def get_security_answer_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.SECURITY_ANSWER_FIELD)

    def get_security_answer_hide_show_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SECURITY_ANSWER_SHOW_HIDE_BTN)

    def get_clubcard_number_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.CLUBCARD_NUMBER_FIELD)

    def get_terms_conditions_agreement_checkbox(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.TERMS_CONDITIONS_AGREEMENT_CHECKBOX)

    def get_about_you_confirm_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ABOUT_YOU_CONFIRM_BTN)

    # Methods to perform actions on get methods

    def enter_email_address_field(self, emailaddress):
        self.get_email_address_field().send_keys(emailaddress)

    def enter_confirm_email_address_field(self, confirmemail):
        self.get_confirm_email_field().send_keys(confirmemail)

    def select_title(self):
        wait = WebDriverWait(self.driver, 20)
        title = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@name, 'ko_unique_4')]")))
        self.driver.execute_script("arguments[0].click();", title)

    def enter_first_name_field(self, fn):
        self.get_first_name_field().send_keys(fn)

    def enter_last_name_field(self, ln):
        self.get_last_name_field().send_keys(ln)

    def enter_dob_date_field(self, dd):
        self.get_dob_date_field().send_keys(dd)

    def enter_dob_month_field(self, mm):
        self.get_dob_month_field().send_keys(mm)

    def enter_dob_year_field(self, yyyy):
        self.get_dob_year_field().send_keys(yyyy)

    def select_type_of_account(self):
        wait = WebDriverWait(self.driver, 20)
        select_account_type = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@name, 'ko_unique_6')]")))
        self.driver.execute_script("arguments[0].click();", select_account_type)

    def enter_contact_number(self, contactno):
        self.get_contact_number_field().send_keys(contactno)

    def enter_current_address_line(self, currentaddressline):
        self.get_current_address_line_field().send_keys(currentaddressline)

    def enter_current_address_postcode(self, currentpostcode):
        self.get_current_address_postcode_field().send_keys(currentpostcode)

    def select_current_find_address_btn(self):
        self.get_find_current_address_btn().click()

    def enter_current_address_month(self, mm):
        self.get_current_address_month_field().send_keys(mm)

    def enter_current_address_year(self, yyyy):
        self.get_current_address_year_field().send_keys(yyyy)
        self.get_current_address_year_field().send_keys(Keys.ENTER)

    def enter_previous_address_line(self, previousaddressline):
        self.get_previous_address_line_field().send_keys(previousaddressline)

    def enter_previous_address_postcode(self, previouspostcode):
        self.get_previous_address_postcode_field().send_keys(previouspostcode)

    def select_previous_find_address_btn(self):
        self.get_previous_find_address_btn().click()

    def enter_previous_address_month(self, mm):
        self.get_previous_address_month_field().send_keys(mm)

    def enter_previous_address_year(self, yyyy):
        self.get_previous_address_year_field().send_keys(yyyy)
        self.get_previous_address_year_field().send_keys(Keys.ENTER)

    def enter_pw_field(self, pw):
        self.get_create_pw_field().send_keys(pw)

    def enter_confirm_pw_field(self, confirmpw):
        self.get_confirm_pw_field().send_keys(confirmpw)

    def select_show_hide_pw_btn(self):
        self.get_show_hide_pw_btn().click()

    def select_security_question(self):
        sq = Select(self.get_security_question_dropdown())
        sq.select_by_visible_text("Your father\'s first name?")

    def enter_security_answer(self, securityanswer):
        self.get_security_answer_field().send_keys(securityanswer)

    def select_security_hide_show_btn(self):
        self.get_security_answer_hide_show_btn().click()

    def enter_clubcard_number(self, clubcardnumber):
        self.get_clubcard_number_field().send_keys(clubcardnumber)

    def select_terms_conditions_agreement_checkbox(self):
        self.get_terms_conditions_agreement_checkbox().click()

    def select_about_you_confirm_btn(self):
        self.get_about_you_confirm_btn().click()


    def enter_email_twice(self, emailaddress, confirmemail):
        self.enter_email_address_field(emailaddress)
        self.enter_confirm_email_address_field(confirmemail)

    def enter_full_name(self, fn, ln):
        self.enter_first_name_field(fn)
        self.enter_last_name_field(ln)

    def enter_dob(self, dd, mm, yyyy):
        self.enter_dob_date_field(dd)
        self.enter_dob_month_field(mm)
        self.enter_dob_year_field(yyyy)

    def enter_current_address(self, currentaddressline, currentpostcode, mm, yyyy):
        self.enter_current_address_line(currentaddressline)
        self.enter_current_address_postcode(currentpostcode)
        self.select_current_find_address_btn()
        self.enter_current_address_month(mm)
        self.enter_current_address_year(yyyy)

    def enter_previous_address(self, previousaddressline, previouspostcode, mm, yyyy):
        self.enter_previous_address_line(previousaddressline)
        self.enter_previous_address_postcode(previouspostcode)
        self.select_previous_find_address_btn()
        self.enter_previous_address_month(mm)
        self.enter_previous_address_year(yyyy)










