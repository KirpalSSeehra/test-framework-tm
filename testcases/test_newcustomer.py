import time

import pytest

from pages.tm_basketpage import BasketPage
from pages.tm_checkoutpage import CheckoutPage
from pages.tm_homepage import HomePage
from pages.tm_catalogue_search import CatalogueSearch
from pages.tm_product_description_page import ProductDescriptionPage


@pytest.mark.usefixtures("setup")
class TestNewCustomer():
    def test_purchase_device(self):

        hp = HomePage(self.driver)
        cs = CatalogueSearch(self.driver)
        pdp = ProductDescriptionPage(self.driver)
        bp = BasketPage(self.driver)
        co = CheckoutPage(self.driver)

        # Accept cookies
        hp.selectAcceptCookiesBtn()

        # Manage cookies
        # hp.selectManageCookiesBtn()
        # hp.selectManageExperienceBtn()
        # time.sleep(1)
        # hp.selectManageAdvertisingBtn()
        # time.sleep(1)
        # hp.selectManageSavePreferencesBtn()
        # time.sleep(1)

        # Scroll down to bottom of page
        # hp.page_scroll()

        # Search for device
        hp.enterSearchBarField("iphone 13")

        # # Scroll down to bottom of page
        # cs.page_scroll()

        # Select first carousel item
        cs.selectDeviceItem()

        # Zoom out of page
        # pdp.page_zoom()

        # Scroll to bottom of pdp page
        # pdp.page_scroll()

        time.sleep(2)

        # Select device colour
        pdp.selectDeviceColourBtn()

        time.sleep(2)

        # Select device storage
        # pdp.selectDeviceStorageBtn()

        pdp.selectTariffSelectorBtn()

        time.sleep(2)

        # Add to basket
        pdp.selectAddToBasketBtn()

        # New customer button click
        pdp.selectNewCustomerBtn()

        # Existing button click
        # pdp.selectExistingCustomerBtn()

        # Enter existing customer details
        # Need to deal with bot pop up thing
        # pdp.enterExistingCustomerEmailField("kirpal-seehra@hotmail.co.uk")
        # pdp.enterExistingCustomerPwField("kips1994")
        # time.sleep(2)
        # pdp.selectExistingCustomerLoginBtn()
        # time.sleep(2)

        # Selecting insurance options
        bp.selectFullCoverBtn()
        time.sleep(2)
        bp.selectInsurancePolicyContinueBtn()
        time.sleep(2)

        # Change contract
        # bp.selectChangePhoneContractBtn()

        # Change safety buffer
        # bp.selectChangeSafetyBufferBtn()

        # Change insurance
        # bp.selectChangeInsuranceBtn()
        # time.sleep(2)
        # bp.selectFullCoverBtn()
        # time.sleep(2)
        # bp.selectNoInsurancePolicyContinueBtn()
        # time.sleep(2)

        # checkout button
        bp.selectGoToCheckoutBtn()

        # Enter email address
        co.enterEmailAddressField("kirpal-seehra@hotmail.co.uk")

        # Confirm email address
        co.enterConfirmEmailAddressField("kirpal-seehra@hotmail.co.uk")

        # Select title
        co.select_title()

        # Enter firstname
        co.enterFirstNameField("Kirpal")

        # Enter lastname
        co.enterLastNameField("Seehra")

        # Enter DOB
        co.enterDobDateField("03")
        co.enterDobMonthField("10")
        co.enterDobYearField("1994")

        # Check Account Type Selected
        # co.check_type_of_account_selected()

        time.sleep(2)

        # Select Account Type
        co.select_type_of_account()

        # co.click_execute_script()

        time.sleep(2)

        # Enter Contact Number
        co.enterContactNumber("07940490912")

        # Enter current address and find address
        co.enterCurrentAddressLine("44")
        co.enterCurrentAddressPostcode("IG3 9JG")
        co.selectCurrentFindAddressBtn()

        # Enter current address month and year
        co.enterCurrentAddressMonth("10")
        co.enterCurrentAddressYear("2021")

        time.sleep(2)

        # Enter previous address and find address
        co.enterPreviousAddressLine("42")
        co.enterPreviousAddressPostcode("IG3 9JG")
        co.selectPreviousAddressBtn()

        # Enter previous address month and year
        co.enterPreviousAddressMonth("10")
        co.enterPreviousAddressYear("2018")

        co.enterPwField("Test0001")
        co.enterConfirmPwField("Test0001")
        co.selectShowHidePwBtn()

        co.selectSecurityQuestion()

        time.sleep(3)

        co.enterSecurityAnswer("red")

        time.sleep(2)

        co.selectSecurityHideShowBtn()

        time.sleep(2)



