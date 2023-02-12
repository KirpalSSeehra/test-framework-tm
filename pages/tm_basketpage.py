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


    def getFullCoverBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FULL_COVER_BTN)

    def getDamageCoverBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DAMAGE_COVER_BTN)

    def getNoInsuranceBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.NO_INSURANCE_BTN)

    def getShowMoreLessBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SHOW_MORE_LESS_BTN)

    def getInsurancePolicyContinueBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.INSURANCE_POLICY_CONTINUE_BTN)

    def getInsurancePolicyBackBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.INSURANCE_POLICY_BACK_BTN)

    def getNoInsurancePolicyContinueBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.NO_INSURANCE_POLICY_CONTINUE_BTN)

    def getNoInsurancePolicyBackBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.NO_INSURANCE_POLICY_BACK_BTN)

    def getChangePhoneContractBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CHANGE_PHONE_CONTRACT_BTN)

    def getChangeSafetyBufferBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CHANGE_SAFETY_BUFFER_BTN)

    def getChangeInsuranceBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CHANGE_INSURANCE_BTN)

    def getGoToCheckoutBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GO_TO_CHECKOUT_BTN)

    def selectFullCoverBtn(self):
        self.getFullCoverBtn().click()

    def selectDamageCoverBtn(self):
        self.getDamageCoverBtn().click()

    def selectNoInsuranceBtn(self):
        self.getNoInsuranceBtn().click()

    def selectShowMoreLessBtn(self):
        self.getShowMoreLessBtn().click()

    def selectInsurancePolicyContinueBtn(self):
        self.getInsurancePolicyContinueBtn().click()

    def selectInsurancePolicyBackBtn(self):
        self.getInsurancePolicyBackBtn().click()

    def selectNoInsurancePolicyContinueBtn(self):
        self.getNoInsurancePolicyContinueBtn().click()

    def selectNoInsurancePolicyBackBtn(self):
        self.getNoInsurancePolicyBackBtn().click()

    def selectChangePhoneContractBtn(self):
        self.getChangePhoneContractBtn().click()

    def selectChangeSafetyBufferBtn(self):
        self.getChangeSafetyBufferBtn().click()

    def selectChangeInsuranceBtn(self):
        self.getChangeInsuranceBtn().click()

    def selectGoToCheckoutBtn(self):
        self.getGoToCheckoutBtn().click()