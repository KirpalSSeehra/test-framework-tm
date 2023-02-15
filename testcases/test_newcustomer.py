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
        hp.select_accept_cookies_btn()

        # Manage cookies
        # hp.select_manage_cookies_btn()
        # hp.select_manage_experience_btn()
        # time.sleep(1)
        # hp.select_manage_advertising_btn()
        # time.sleep(1)
        # hp.select_manage_save_preferences_btn()
        # time.sleep(1)

        # Scroll down to bottom of page
        # hp.page_scroll()

        # Search for device
        hp.enter_search_bar_field("iphone 13")

        # # Scroll down to bottom of page
        # cs.page_scroll()

        # Select first carousel item
        cs.select_device_item()

        # Zoom out of page
        # pdp.page_zoom()

        # Scroll to bottom of pdp page
        # pdp.page_scroll()

        time.sleep(2)

        # Select device colour
        pdp.select_device_colour_btn()

        time.sleep(2)

        # Select device storage
        # pdp.selectDeviceStorageBtn()

        pdp.select_tariff_selector_btn()

        time.sleep(2)

        # Add to basket
        pdp.select_add_to_basket_btn()

        # New customer button click
        pdp.select_new_customer_btn()

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
        bp.select_full_cover_btn()
        time.sleep(2)
        bp.select_insurance_policy_continue_btn()
        time.sleep(2)

        # Change contract
        # bp.select_change_phone_contract_btn()

        # Change safety buffer
        # bp.select_change_safety_buffer_btn()

        # Change insurance
        # bp.select_change_insurance_btn()
        # time.sleep(2)
        # bp.select_full_cover_btn()
        # time.sleep(2)
        # bp.select_no_insurance_policy_continue_btn()
        # time.sleep(2)

        # checkout button
        bp.select_go_to_checkout_btn()

        # Enter email address and confirm email
        co.enter_email_twice("kirpal-seehra@hotmail.co.uk", "kirpal-seehra@hotmail.co.uk")

        # Select title
        co.select_title()

        # Enter Fullname
        co.enter_full_name("Kirpal", "Seehra")

        # Enter DOB
        co.enter_dob("03", "10", "1994")

        # Check Account Type Selected
        # co.check_type_of_account_selected()

        time.sleep(2)

        # Select Account Type
        # co.select_type_of_account()

        # co.click_execute_script()

        time.sleep(2)

        # Enter Contact Number
        co.enter_contact_number("07940490912")

        # Enter current address and find address. Enter current address month and year.
        co.enter_current_address("44", "IG3 9JG", "10", "2021")

        time.sleep(2)

        # Enter previous address and find address. Enter previous address month and year.
        co.enter_previous_address("42", "IG3 9JG", "10", "2018")

        time.sleep(2)

        co.enter_pw_field("Test0001")
        co.enter_confirm_pw_field("Test0001")
        co.select_show_hide_pw_btn()

        co.select_security_question()

        time.sleep(3)

        co.enter_security_answer("red")

        time.sleep(2)

        co.select_security_hide_show_btn()

        time.sleep(2)



