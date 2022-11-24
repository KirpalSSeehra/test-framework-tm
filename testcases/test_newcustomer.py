import time

import pytest

from pages.tm_basketpage import BasketPage
from pages.tm_homepage import HomePage
from pages.tm_catalogue_search import CatalogueSearch
from pages.tm_product_description_page import ProductDescriptionPage


@pytest.mark.usefixtures("setup")
class TestNewCustomer():
    def test_purchase_device(self):

        hp = HomePage(self.driver, self.wait)
        cs = CatalogueSearch(self.driver, self.wait)
        pdp = ProductDescriptionPage(self.driver, self.wait)
        bp = BasketPage(self.driver, self.wait)

        # Accept cookies
        hp.click_cookies()

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
        time.sleep(5)
