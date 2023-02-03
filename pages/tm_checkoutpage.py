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
    DOB_DATE_FIELD = "customer-day"
    DOB_MONTH_FIELD = "customer-month"
    DOB_YEAR_FIELD = "customer-year"
    # SELECT_ACCOUNT_TYPE_BTN
    CONTACT_NO_FIELD = "customer[tm_contact_number]"
    CURRENT_ADDRESS_LINE_FIELD = "billing_address[tm_building_id]"
    CURRENT_POSTCODE_FIELD = "billing_address[postcode]"
    FIND_CURRENT_ADDRESS_BTN = "//a[contains(@data-bind, 'click: findAddress')]"
    CURRENT_ADDRESS_MONTH_FIELD = "billing_address[tm_start_date][month]"
    CURRENT_ADDRESS_YEAR_FIELD = "billing_address[tm_start_date][year]"
    PREVIOUS_ADDRESS_LINE_FIELD = "previous_address[tm_building_id]"
    PREVIOUS_POSTCODE_FIELD = "previous_address[postcode]"
    FIND_PREVIOUS_ADDRESS_BTN = "//*[@id='about-form']/fieldset[2]/div[4]/a"
    PREVIOUS_ADDRESS_MONTH_FIELD = "previous_address[tm_start_date][month]"
    PREVIOUS_ADDRESS_YEAR_FIELD = "previous_address[tm_start_date][year]"
    CREATE_PW_FIELD = "customer-password"
    CONFIRM_PW_FIELD = "customer-confirm-password"
    SHOW_HIDE_PW_BTN = "//a[contains(@data-bind, 'click: showHidePassword')]"
    SECURITY_QUESTION_DROPDOWN = "//select[@name='account[tm_security_question]']"
    SECURITY_ANSWER_FIELD = "account[tm_security_answer]"
    SECURITY_ANSWER_SHOW_HIDE_BTN = "//a[contains(@data-bind, 'click: showHideAnswer')]"

    # Get Methods
    def getEmailAddressField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EMAIL_ADDRESS_FIELD)

    def getConfirmEmailField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CONFIRM_EMAIL_ADDRESS_FIELD)

    def getFirstNameField(self):
        return self.wait_until_element_is_clickable(By.NAME, self.FIRST_NAME_FIELD)

    def getLastNameField(self):
        return self.wait_until_element_is_clickable(By.NAME, self.LAST_NAME_FIELD)

    def getDobDateField(self):
        return self.wait_until_element_is_clickable(By.ID, self.DOB_DATE_FIELD)

    def getDobMonthField(self):
        return self.wait_until_element_is_clickable(By.ID, self.DOB_MONTH_FIELD)

    def getDobYearField(self):
        return self.wait_until_element_is_clickable(By.ID, self.DOB_YEAR_FIELD)

    def getContactNumberField(self):
        return self.wait_until_element_is_clickable(By.NAME, self.CONTACT_NO_FIELD)

    def getCurrentAddressLineField(self):
        return self.wait_until_element_is_clickable(By.NAME, self.CURRENT_ADDRESS_LINE_FIELD)

    def getCurrentAddressPostcodeField(self):
        return self.wait_until_element_is_clickable(By.NAME, self.CURRENT_POSTCODE_FIELD)

    def getFindCurrentAddressBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FIND_CURRENT_ADDRESS_BTN)

    def getCurrentAddressMonthField(self):
        return self.wait_until_element_is_clickable(By.NAME, self.CURRENT_ADDRESS_MONTH_FIELD)

    def getCurrentAddressYearField(self):
        return self.wait_until_element_is_clickable(By.NAME, self.CURRENT_ADDRESS_YEAR_FIELD)

    def getPreviousAddressLineField(self):
        return self.wait_until_element_is_clickable(By.NAME, self.PREVIOUS_ADDRESS_LINE_FIELD)

    def getPreviousAddressPostcodeField(self):
        return self.wait_until_element_is_clickable(By.NAME, self.PREVIOUS_POSTCODE_FIELD)

    def getFindPreviousAddressBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FIND_PREVIOUS_ADDRESS_BTN)

    def getPreviousAddressMonthField(self):
        return self.wait_until_element_is_clickable(By.NAME, self.PREVIOUS_ADDRESS_MONTH_FIELD)

    def getPreviousAddressYearField(self):
        return self.wait_until_element_is_clickable(By.NAME, self.PREVIOUS_ADDRESS_YEAR_FIELD)

    def getCreatePwField(self):
        return self.wait_until_element_is_clickable(By.ID, self.CREATE_PW_FIELD)

    def getConfirmPwField(self):
        return self.wait_until_element_is_clickable(By.ID, self.CONFIRM_PW_FIELD)

    def getShowHidePwBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SHOW_HIDE_PW_BTN)

    def getSecurityQuestionDropdown(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SECURITY_QUESTION_DROPDOWN)

    def getSecurityAnswerField(self):
        return self.wait_until_element_is_clickable(By.NAME, self.SECURITY_ANSWER_FIELD)

    def getSecurityAnswerHideShowBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SECURITY_ANSWER_SHOW_HIDE_BTN)

    # Action methods

    def enterEmailAddressField(self, emailaddress):
        self.getEmailAddressField().send_keys(emailaddress)

    def enterConfirmEmailAddressField(self, confirmemail):
        self.getConfirmEmailField().send_keys(confirmemail)

    def select_title(self):
        wait = WebDriverWait(self.driver, 20)
        title = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@name, 'ko_unique_4')]")))
        self.driver.execute_script("arguments[0].click();", title)

    def enterFirstNameField(self, fn):
        self.getFirstNameField().send_keys(fn)

    def enterLastNameField(self, ln):
        self.getLastNameField().send_keys(ln)

    def enterDobDateField(self, dd):
        self.getDobDateField().send_keys(dd)

    def enterDobMonthField(self, mm):
        self.getDobMonthField().send_keys(mm)

    def enterDobYearField(self, yyyy):
        self.getDobYearField().send_keys(yyyy)

    def select_type_of_account(self):
        wait = WebDriverWait(self.driver, 20)
        select_account_type = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@name, 'ko_unique_6')]")))
        self.driver.execute_script("arguments[0].click();", select_account_type)

    def enterContactNumber(self, contactno):
        self.getContactNumberField().send_keys(contactno)

    def enterCurrentAddressLine(self, currentaddressline):
        self.getCurrentAddressLineField().send_keys(currentaddressline)

    def enterCurrentAddressPostcode(self, currentpostcode):
        self.getCurrentAddressPostcodeField().send_keys(currentpostcode)

    def selectCurrentFindAddressBtn(self):
        self.getFindCurrentAddressBtn().click()

    def enterCurrentAddressMonth(self, mm):
        self.getCurrentAddressMonthField().send_keys(mm)

    def enterCurrentAddressYear(self, yyyy):
        self.getCurrentAddressYearField().send_keys(yyyy)
        self.getCurrentAddressYearField().send_keys(Keys.ENTER)

    def enterPreviousAddressLine(self, previousaddressline):
        self.getPreviousAddressLineField().send_keys(previousaddressline)

    def enterPreviousAddressPostcode(self, previouspostcode):
        self.getPreviousAddressPostcodeField().send_keys(previouspostcode)

    def selectPreviousAddressBtn(self):
        self.getFindPreviousAddressBtn().click()

    def enterPreviousAddressMonth(self, mm):
        self.getPreviousAddressMonthField().send_keys(mm)

    def enterPreviousAddressYear(self, yyyy):
        self.getPreviousAddressYearField().send_keys(yyyy)
        self.getPreviousAddressYearField().send_keys(Keys.ENTER)

    def enterPwField(self, pw):
        self.getCreatePwField().send_keys(pw)

    def enterConfirmPwField(self, confirmpw):
        self.getConfirmPwField().send_keys(confirmpw)

    def selectShowHidePwBtn(self):
        self.getShowHidePwBtn().click()

    def selectSecurityQuestion(self):
        sq = Select(self.getSecurityQuestionDropdown())
        sq.select_by_visible_text("Your father\'s first name?")

    def enterSecurityAnswer(self, securityanswer):
        self.getSecurityAnswerField().send_keys(securityanswer)

    def selectSecurityHideShowBtn(self):
        self.getSecurityAnswerHideShowBtn().click()










