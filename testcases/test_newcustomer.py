import time

import pytest
import softest
from selenium.webdriver.common.by import By

from pages.tm_homepage import HomePage
from pages.tm_product_description_page import ProductDescriptionPage
from utilities.utils import Utils
from ddt import ddt, data, file_data, unpack


@pytest.mark.usefixtures("setup")
@ddt
class TestNewCustomer(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = HomePage(self.driver)
        self.pdp = ProductDescriptionPage(self.driver)
        self.ut = Utils()

    @file_data("../testdata/testdata.json")
    def test_ddt_search_json(self, search_result):
        self.hp.select_accept_cookies_btn()
        catalogue_search = self.hp.enter_search_bar_field(search_result)
        catalogue_search.select_device_item()
        time.sleep(2)

    def test_new_customer_journey_e2e(self):
        # Accept cookies
        self.hp.select_accept_cookies_btn()

        # Scroll down to bottom of page
        # hp.page_scroll()

        # Search for device
        catalogue_search = self.hp.enter_search_bar_field("iphone 13")

        all_devices = catalogue_search.wait_for_presence_of_all_elements(By.XPATH, "//h3[contains(text(),'13')]")
        print(len(all_devices))

        self.ut.assert_in_list_item_text(all_devices, "13")

        time.sleep(2)

        # Select first carousel item
        catalogue_search.select_device_item()

        # Zoom out of page
        # pdp.page_zoom()

        time.sleep(2)

        # Select device colour
        self.pdp.select_device_colour_btn()

        time.sleep(2)

        # Select device storage
        # pdp.selectDeviceStorageBtn()

        self.pdp.select_tariff_selector_btn()

        time.sleep(2)

        # Add to basket
        self.pdp.select_add_to_basket_btn()

        # New customer button click
        basket_page = self.pdp.select_new_customer_btn()

        # Selecting insurance options
        basket_page.select_full_cover_btn()
        time.sleep(2)
        basket_page.select_insurance_policy_continue_btn()
        time.sleep(2)

        # Change contract
        # basket_page.select_change_phone_contract_btn()

        # Change safety buffer
        # basket_page.select_change_safety_buffer_btn()

        # Change insurance
        # basket_page.select_change_insurance_btn()
        # time.sleep(2)
        # basket_page.select_full_cover_btn()
        # time.sleep(2)
        # basket_page.select_no_insurance_policy_continue_btn()
        # time.sleep(2)

        # checkout button
        checkout_page = basket_page.select_go_to_checkout_btn()

        # Enter email address and confirm email
        checkout_page.enter_email_twice("kirpal-seehra@hotmail.co.uk", "kirpal-seehra@hotmail.co.uk")

        # Select title
        checkout_page.select_title()

        # Enter Fullname
        checkout_page.enter_full_name("Kirpal", "Seehra")

        # Enter DOB
        checkout_page.enter_dob("03", "10", "1994")

        time.sleep(2)

        # Select Account Type
        # checkout_page.select_type_of_account()

        # checkout_page.click_execute_script()

        time.sleep(2)

        # Enter Contact Number
        checkout_page.enter_contact_number("07940490912")

        # Enter current address and find address. Enter current address month and year.
        checkout_page.enter_current_address("44", "IG3 9JG", "10", "2021")

        time.sleep(2)

        # Enter previous address and find address. Enter previous address month and year.
        checkout_page.enter_previous_address("42", "IG3 9JG", "10", "2018")

        time.sleep(2)

        checkout_page.enter_pw_field("Test0001")
        checkout_page.enter_confirm_pw_field("Test0001")
        checkout_page.select_show_hide_pw_btn()

        checkout_page.select_security_question()

        time.sleep(3)

        checkout_page.enter_security_answer("red")

        time.sleep(2)

        checkout_page.select_security_hide_show_btn()
        checkout_page.enter_clubcard_number("634004024066936008")
        checkout_page.select_terms_conditions_agreement_checkbox()
        time.sleep(5)

        checkout_page.select_about_you_confirm_btn()
        time.sleep(5)

    def test_existing_customer_journey_e2e(self):

        self.hp.select_manage_cookies_btn()
        self.hp.select_manage_experience_btn()
        time.sleep(1)
        self.hp.select_manage_advertising_btn()
        time.sleep(1)
        self.hp.select_manage_save_preferences_btn()
        time.sleep(1)

        catalogue_search = self.hp.enter_search_bar_field("iphone 13")
        catalogue_search.select_device_item()

        self.pdp.select_device_colour_btn()
        self.pdp.select_tariff_selector_btn()
        time.sleep(1)
        self.pdp.select_add_to_basket_btn()

        # Existing customer button click
        self.pdp.select_existing_customer_btn()

        # Enter existing customer details
        self.pdp.enter_existing_customer_email_field("kirpal-seehra@hotmail.co.uk")
        self.pdp.enter_existing_customer_pw_field("kips1994")
        self.pdp.select_existing_customer_login_btn()
        time.sleep(5)
