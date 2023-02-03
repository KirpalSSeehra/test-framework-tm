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
        hp.accept_cookies()

        # Manage cookies
        # hp.manage_cookies()

        # Scroll down to bottom of page
        # hp.page_scroll()

        # Search for device
        hp.search_device("iphone 13")

        # # Scroll down to bottom of page
        # cs.page_scroll()

        # Select first carousel item
        cs.select_device()

        # Zoom out of page
        # pdp.page_zoom()

        # Scroll to bottom of pdp page
        # pdp.page_scroll()

        time.sleep(2)

        # Select device colour
        pdp.select_device_colour()

        time.sleep(2)

        # Select device storage
        # pdp.select_device_storage()

        time.sleep(2)

        # Add to basket
        pdp.click_add_to_basket()

        # New customer button click
        pdp.select_new_customer()

        # Existing button click
        # pdp.select_existing_customer()

        # Enter existing customer details
        # Need to deal with bot pop up thing
        # pdp.enter_existing_customer_details("kirpal-seehra@hotmail.co.uk", "kips1994")

        # Select full insurance
        bp.select_full_insurance()

        # Change contract
        # bp.change_phone_contract()

        # Change safety buffer
        # bp.change_safety_buffer()

        # Change insurance
        # bp.change_insurance()
        time.sleep(2)

        # checkout button
        bp.click_checkout()

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



