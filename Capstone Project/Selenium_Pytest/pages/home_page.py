import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class HomePage(BasePage):

    SEARCH_BOX      = (By.ID,          "small-searchterms")
    SEARCH_BTN      = (By.XPATH,       "//input[@value='Search']")
    RESULT_ITEMS    = (By.CSS_SELECTOR, "div.product-item")
    PRODUCT_TITLES  = (By.CSS_SELECTOR, "h2.product-title a")
    CART_QTY_BADGE  = (By.CSS_SELECTOR, "span.cart-qty")


    def search(self, keyword):
        logger.info(f"SEARCH: '{keyword}' ")

        self.type_text(*self.SEARCH_BOX, keyword)
        assert self.get_value(*self.SEARCH_BOX) == keyword, \
            f"Search box value mismatch – expected '{keyword}'"

        self.click(*self.SEARCH_BTN)

        assert self.wait_for_url("search"), \
            "Search results URL does not contain 'search'"
        logger.info("Search submitted – on results page")

    def assert_results_exist(self):
        assert self.is_visible(*self.RESULT_ITEMS), \
            "No search results found – result items not visible"
        count = len(self.driver.find_elements(*self.RESULT_ITEMS))
        assert count > 0, "Search result count is 0"
        logger.info(f"{count} search result(s) found")
        return count

    def get_product_titles(self):
        titles = [el.text for el in self.driver.find_elements(*self.PRODUCT_TITLES)]
        logger.info(f"Product titles on page: {titles}")
        return titles

    def click_product(self, product_name):
        assert self.is_visible(*self.PRODUCT_TITLES), "No product titles visible"
        elements = self.driver.find_elements(*self.PRODUCT_TITLES)
        assert elements, "Product title elements list is empty"

        for el in elements:
            if product_name.lower() in el.text.lower():
                name = el.text
                el.click()
                logger.info(f"Clicked product: '{name}'")
                return name

        # Fallback: click first result
        name = elements[0].text
        elements[0].click()
        logger.info(f"Exact match not found – clicked first result: '{name}'")
        return name
