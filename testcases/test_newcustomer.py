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
        hp.click_cookies()

        # Scroll down to bottom of page
        # hp.page_scroll()

        # Search for device
        hp.search_device("iphone 12")

        # # Scroll down to bottom of page
        # cs.page_scroll()

        # Select first carousel item
        cs.select_device()

        # Zoom out of page
        # pdp.page_zoom()

        # Scroll to bottom of pdp page
        # pdp.page_scroll()

        # Select device colour
        # pdp.select_device_colour()

        # Select device storage
        # pdp.select_device_storage()

        # Add to basket
        pdp.click_add_to_basket()

        # New customer button click
        pdp.select_type_of_customer()

        # Select insurance
        bp.select_insurance()

        # Change contract
        # bp.change_phone_contract()

        # checkout button
        bp.click_checkout()

        # Enter email address
        co.enter_email_address("kirpal-seehra@hotmail.co.uk")

        # Confirm email address
        co.confirm_email_address("kirpal-seehra@hotmail.co.uk")

        # Select title
        co.select_title()

        # Enter firstname
        co.enter_firstname("Kirpal")

        # Enter lastname
        co.enter_lastname("Seehra")

        # Enter DOB
        co.enter_dob("03", "10", "1994")

        # Check Account Type Selected
        # co.check_type_of_account_selected()

        # Select Account Type
        co.select_type_of_account()

        # Enter Contact Number
        co.enter_contact_number("07940490912")

        # Enter Address and find address
        co.enter_address("44", "IG3 9JG")
        co.find_address()

        time.sleep(5)