import time
import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class CartPage(BasePage):

    CART_ROWS     = (By.CSS_SELECTOR, "tr.cart-item-row")
    PRODUCT_NAMES = (By.CSS_SELECTOR, "td.product a")
    QTY_INPUTS    = (By.CSS_SELECTOR, "input.qty-input")
    REMOVE_CHECKS = (By.CSS_SELECTOR, "input[name='removefromcart']")
    UPDATE_BTN    = (By.XPATH,        "//input[@name='updatecart']")
    EMPTY_MSG     = (By.CSS_SELECTOR, "div.no-data")

    def item_count(self):
        rows = self.driver.find_elements(*self.CART_ROWS)
        return len(rows)

    def product_names_in_cart(self):
        els = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [el.text for el in els]

    def get_qty_at(self, index=0):
        inputs = self.driver.find_elements(*self.QTY_INPUTS)
        assert index < len(inputs), \
            f"No cart item at index {index} - only {len(inputs)} item(s)"
        return inputs[index].get_attribute("value")

    def assert_not_empty(self):
        count = self.item_count()
        assert count > 0, "Cart is empty"
        logger.info(f"Cart has {count} item(s)")
        return count

    def assert_product_present(self, product_name):
        names = self.product_names_in_cart()
        assert any(product_name.lower() in n.lower() for n in names), \
            f"'{product_name}' not found in cart. Found: {names}"
        logger.info(f"Product '{product_name}' confirmed in cart")

    def assert_qty_equals(self, expected_qty, index=0):
        actual = self.get_qty_at(index)
        assert actual == str(expected_qty), \
            f"Qty at index {index} expected '{expected_qty}', got '{actual}'"
        logger.info(f"Quantity at index {index} confirmed: {actual}")

    def update_quantity(self, new_qty, index=0):
        logger.info(f"UPDATE CART QTY to {new_qty} (index {index})")
        self.assert_not_empty()
        inputs = self.driver.find_elements(*self.QTY_INPUTS)
        assert index < len(inputs), \
            f"Cannot update index {index} - only {len(inputs)} item(s) in cart"
        inputs[index].clear()
        inputs[index].send_keys(str(new_qty))
        assert inputs[index].get_attribute("value") == str(new_qty), \
            f"Qty field not updated to '{new_qty}' before clicking Update"
        self.click(*self.UPDATE_BTN)
        # Wait for page to reload after update
        time.sleep(2)
        self.assert_qty_equals(new_qty, index)
        logger.info(f"Cart quantity updated to {new_qty}")

    def remove_item(self, index=0):
        logger.info(f"REMOVE ITEM (index {index})")
        count_before = self.assert_not_empty()

        checkboxes = self.driver.find_elements(*self.REMOVE_CHECKS)
        assert len(checkboxes) > 0, "No remove checkboxes found"
        assert index < len(checkboxes), \
            f"No remove checkbox at index {index} - only {len(checkboxes)} item(s)"

        checkboxes[index].click()
        logger.info("Remove checkbox checked")

        self.click(*self.UPDATE_BTN)

        # Wait for page to reload after removal
        time.sleep(3)

        count_after = self.item_count()
        assert count_after < count_before, \
            f"Item not removed. Before={count_before}, After={count_after}"
        logger.info(f"Item removed. Cart count: {count_before} to {count_after}")

        if count_after == 0:
            logger.info("Cart is now empty")

        return count_after

    def clear_cart(self, base_url):
        self.driver.get(f"{base_url}/cart")
        time.sleep(1)

        count = self.item_count()
        if count == 0:
            logger.info("Cart is already empty — nothing to clear")
            return

        logger.info(f"Clearing {count} leftover item(s) from cart")
        checkboxes = self.driver.find_elements(*self.REMOVE_CHECKS)
        for checkbox in checkboxes:
            checkbox.click()

        self.click(*self.UPDATE_BTN)
        time.sleep(2)

        remaining = self.item_count()
        assert remaining == 0, \
            f"Cart clear failed — {remaining} item(s) still remain"
        logger.info("Cart cleared successfully")