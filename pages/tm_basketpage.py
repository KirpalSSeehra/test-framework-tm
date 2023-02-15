from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class BasketPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    FULL_COVER_BTN = "//*[@id='tm-insurance-content']/div[2]/div[3]/div[2]/div[5]/fieldset/div/div/div[2]/input"
    DAMAGE_COVER_BTN = "//*[@id='tm-insurance-content']/div[2]/div[3]/div[2]/div[5]/fieldset/div/div/div[1]/input"
    NO_INSURANCE_BTN = "//*[@id='tm-insurance-content']/div[2]/div[4]/fieldset/div/div/div/input"
    SHOW_MORE_LESS_BTN = "//*[@id='tm-insurance-content']/div[2]/div[3]/div[3]/div"
    INSURANCE_POLICY_CONTINUE_BTN = "//*[@id='tm-insurance-content']/div[3]/div[2]/div[1]"
    INSURANCE_POLICY_BACK_BTN = "//*[@id='tm-insurance-content']/div[3]/div[2]/div[2]"
    NO_INSURANCE_POLICY_CONTINUE_BTN = "//*[@id='tm-insurance-content']/div[4]/div[2]/div[1]"
    NO_INSURANCE_POLICY_BACK_BTN = "//*[@id='tm-insurance-content']/div[4]/div[2]/div[2]"

    CHANGE_PHONE_CONTRACT_BTN = "//*[@id='maincontent']/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[1]/a[2]"
    CHANGE_SAFETY_BUFFER_BTN = "//*[@id='maincontent']/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/a"
    CHANGE_INSURANCE_BTN = "//*[@id='maincontent']/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/a"

    GO_TO_CHECKOUT_BTN = "//button[@title='Go to checkout']"


    def get_full_cover_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FULL_COVER_BTN)

    def get_damage_cover_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DAMAGE_COVER_BTN)

    def get_no_insurance_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.NO_INSURANCE_BTN)

    def get_show_more_less_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SHOW_MORE_LESS_BTN)

    def get_insurance_policy_continue_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.INSURANCE_POLICY_CONTINUE_BTN)

    def get_insurance_policy_back_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.INSURANCE_POLICY_BACK_BTN)

    def get_no_insurance_policy_continue_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.NO_INSURANCE_POLICY_CONTINUE_BTN)

    def get_no_insurance_policy_back_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.NO_INSURANCE_POLICY_BACK_BTN)

    def get_change_phone_contract_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CHANGE_PHONE_CONTRACT_BTN)

    def get_change_safety_buffer_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CHANGE_SAFETY_BUFFER_BTN)

    def get_change_insurance_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CHANGE_INSURANCE_BTN)

    def get_go_to_checkout_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GO_TO_CHECKOUT_BTN)

    def select_full_cover_btn(self):
        self.get_full_cover_btn().click()

    def select_damage_cover_btn(self):
        self.get_damage_cover_btn().click()

    def select_no_insurance_btn(self):
        self.get_no_insurance_btn().click()

    def select_show_more_less_btn(self):
        self.get_show_more_less_btn().click()

    def select_insurance_policy_continue_btn(self):
        self.get_insurance_policy_continue_btn().click()

    def select_insurance_policy_back_btn(self):
        self.get_insurance_policy_back_btn().click()

    def select_no_insurance_policy_continue_btn(self):
        self.get_no_insurance_policy_continue_btn().click()

    def select_no_insurance_policy_back_btn(self):
        self.get_no_insurance_policy_back_btn().click()

    def select_change_phone_contract_btn(self):
        self.get_change_phone_contract_btn().click()

    def select_change_safety_buffer_btn(self):
        self.get_change_safety_buffer_btn().click()

    def select_change_insurance_btn(self):
        self.get_change_insurance_btn().click()

    def select_go_to_checkout_btn(self):
        self.get_go_to_checkout_btn().click()