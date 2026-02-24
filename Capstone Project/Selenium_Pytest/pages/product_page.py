import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class ProductPage(BasePage):

    PRODUCT_NAME        = (By.CSS_SELECTOR, "div.product-name h1")
    PRODUCT_PRICE       = (By.CSS_SELECTOR, "div.product-price span")
    QTY_INPUT           = (By.CSS_SELECTOR, "input.qty-input")
    ADD_TO_CART_BTN     = (By.XPATH,        "//input[@value='Add to cart']")
    SUCCESS_NOTIF       = (By.CSS_SELECTOR, "div.bar-notification.success p.content")
    CART_LINK_IN_NOTIF  = (By.XPATH,        "//a[text()='shopping cart']")


    def assert_on_product_page(self):
        assert self.is_visible(*self.PRODUCT_NAME), \
            "Product name not visible – may not be on a product detail page"
        name = self.get_text(*self.PRODUCT_NAME)
        assert name, "Product name text is empty"
        logger.info(f"On product detail page: '{name}'")
        return name

    def get_price(self):
        if self.is_visible(*self.PRODUCT_PRICE, timeout=5):
            price = self.get_text(*self.PRODUCT_PRICE)
            assert price, "Product price is empty"
            logger.info(f"Product price: {price}")
            return price
        return "N/A"

    def set_quantity(self, qty):
        qty_str = str(qty)
        if self.is_visible(*self.QTY_INPUT, timeout=3):
            self.type_text(*self.QTY_INPUT, qty_str)
            assert self.get_value(*self.QTY_INPUT) == qty_str, \
                f"Quantity input mismatch – expected '{qty_str}'"
            logger.info(f"Quantity set to {qty}")

    def add_to_cart(self, qty=1):
        logger.info(f"ADD TO CART (qty={qty})")

        self.set_quantity(qty)
        self.click(*self.ADD_TO_CART_BTN)

        assert self.is_visible(*self.SUCCESS_NOTIF, timeout=15), \
            "Success notification not visible after clicking Add to Cart"
        notif = self.get_text(*self.SUCCESS_NOTIF)
        assert notif, "Success notification text is empty"
        assert "cart" in notif.lower(), \
            f"Unexpected notification text: '{notif}'"
        logger.info(f" Added to cart. Notification: '{notif}'")
        return notif

    def go_to_cart(self):
        assert self.is_visible(*self.CART_LINK_IN_NOTIF, timeout=10), \
            "Shopping cart link not visible in notification bar"
        self.click(*self.CART_LINK_IN_NOTIF)
        assert self.wait_for_url("cart"), \
            "Did not navigate to cart page after clicking notification link"
        logger.info("Navigated to shopping cart")
