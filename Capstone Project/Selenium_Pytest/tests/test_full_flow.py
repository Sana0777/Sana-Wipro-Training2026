import time
import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import set_step
from utilities.helper import load_data
from utilities.browser import get_base_url
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

logger = logging.getLogger(__name__)


def generate_ids(data):
    return [f"User_{i+1}" for i in range(len(data))]


_data = load_data()


@pytest.mark.parametrize(
    "first_name, last_name, email, password, gender, "
    "product_search, product_name, add_quantity, updated_quantity",
    _data,
    ids=generate_ids(_data),
)
def test_full_flow(
    driver, request,
    first_name, last_name, email, password, gender,
    product_search, product_name, add_quantity, updated_quantity
):
    base_url     = get_base_url()
    reg_page     = RegistrationPage(driver)
    login_page   = LoginPage(driver)
    home_page    = HomePage(driver)
    product_page = ProductPage(driver)
    cart_page    = CartPage(driver)

    #  STEP 1: Verify site loaded
    set_step("step1_site_loaded", request)
    assert base_url in driver.current_url, \
        f"Browser is not on the expected site. Current URL: {driver.current_url}"
    assert driver.title, "Page title is empty - site may not have loaded"

    # STEP 2: Register
    set_step("step2_register", request)
    reg_result = reg_page.register(first_name, last_name, email, password, gender)
    assert reg_result in ("registered", "already_exists"), \
        f"Registration returned unexpected result: {reg_result}"
    logger.info(f"Registration result for {email}: {reg_result}")

    #  STEP 3: Login
    set_step("step3_login", request)
    driver.get(base_url)
    WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.header-links"))
    )

    if login_page.is_logged_in():
        logger.info("Auto-session detected — logging out to show fresh login")
        login_page.logout()
        driver.get(base_url)
        WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.header-links"))
        )

    # Always perform visible login in the UI
    logger.info(f"Navigating to login page for {email}")
    login_page.navigate_to_login()
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login_button()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a.account"))
    )
    account_text = login_page.get_logged_in_user()
    assert account_text, \
        f"Login failed — account link not visible after login for {email}"
    logger.info(f"Login successful. Account header: '{account_text}'")

    assert "login" not in driver.current_url.lower(), \
        f"Unexpectedly still on login page: {driver.current_url}"

    cart_page.clear_cart(base_url)
    driver.get(base_url)

    # STEP 4: Search for product
    set_step("step4_search_product", request)
    home_page.search(product_search)
    result_count = home_page.assert_results_exist()
    assert result_count > 0, f"No results for '{product_search}'"
    titles = home_page.get_product_titles()
    assert titles, "Product title list is empty on search results page"

    # STEP 5: Open product detail
    set_step("step5_open_product", request)
    clicked_name = home_page.click_product(product_name)
    assert clicked_name, "Clicked product name is empty"
    actual_product_name = product_page.assert_on_product_page()
    assert actual_product_name, "Product name is empty on detail page"
    price = product_page.get_price()
    assert price, "Product price is empty on detail page"

    #  STEP 6: Add to cart
    set_step("step6_add_to_cart", request)
    notification = product_page.add_to_cart(qty=add_quantity)
    assert "cart" in notification.lower(), \
        f"Unexpected add-to-cart notification: '{notification}'"

    # STEP 7: Navigate to cart and verify
    set_step("step7_verify_cart", request)
    product_page.go_to_cart()
    cart_page.assert_not_empty()
    cart_page.assert_product_present(actual_product_name)
    initial_qty = cart_page.get_qty_at(0)
    assert initial_qty == str(add_quantity), \
        f"Initial cart qty mismatch: expected '{add_quantity}', got '{initial_qty}'"

    # STEP 8: Update quantity
    set_step("step8_update_quantity", request)
    cart_page.update_quantity(updated_quantity, index=0)
    cart_page.assert_qty_equals(updated_quantity, index=0)

    # STEP 9: Remove item from cart
    set_step("step9_remove_item", request)
    remaining = cart_page.remove_item(index=0)
    assert remaining == 0, \
        f"Expected 0 items after removal, but {remaining} item(s) remain"

    # STEP 10: Logout
    set_step("step10_logout", request)
    login_page.logout()
    logger.info(f"Test complete for {email}")
