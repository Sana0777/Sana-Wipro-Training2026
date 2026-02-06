import pytest
from selenium import webdriver
from LabBook11 import LabBookPage
import time

class TestLabBook:

    def setup_method(self):

        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(10)

        self.page = LabBookPage(self.driver)

        self.page.open_site()

    def teardown_method(self):

        self.driver.quit()

    def test_lab3_flow(self):

        self.page.open_mac_page()

        self.page.sort_name_az()

        self.page.add_to_cart()

        time.sleep(2)

        assert "Mac" in self.driver.title

    def test_lab4_flow(self):
        # Verify Title
        assert "Your Store" in self.driver.title

        # Go to Mac Page
        self.page.open_mac_page()

        # Verify Mac Heading (After Click Mac)
        assert self.page.verify_mac_heading()

        # Sort Name A-Z
        self.page.sort_name_az()

        # Add to Cart
        self.page.add_to_cart()

        # -------- FIRST SEARCH : Mobile --------
        self.page.search_product("Mobile")

        time.sleep(2)

        # Clear Search
        self.page.clear_search()

        # Click Description Checkbox
        self.page.click_description()

        # Search Again (with Mobile)
        self.page.click_search_again()

        time.sleep(2)

        # -------- SECOND SEARCH : Monitors --------
        self.page.clear_search()

        self.page.search_product("Monitors")

        time.sleep(2)

        # Final Search
        self.page.click_search_again()

        time.sleep(2)
