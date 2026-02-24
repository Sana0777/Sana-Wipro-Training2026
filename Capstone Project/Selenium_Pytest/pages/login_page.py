import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class LoginPage(BasePage):

    LOGIN_LINK   = (By.XPATH,        "//a[text()='Log in']")
    EMAIL        = (By.ID,           "Email")
    PASSWORD     = (By.ID,           "Password")
    LOGIN_BTN    = (By.XPATH,        "//input[@value='Log in']")
    ERROR_MSG    = (By.CSS_SELECTOR, "div.validation-summary-errors span")
    ACCOUNT_LINK = (By.CSS_SELECTOR, "a.account")
    LOGOUT_LINK  = (By.XPATH,        "//a[text()='Log out']")

    def is_logged_in(self):
        return self.is_visible(*self.ACCOUNT_LINK, timeout=3)

    def navigate_to_login(self):
        self.go_to_login()

    def click_login_button(self):
        self.submit_login()

    def go_to_login(self):
        self.click(*self.LOGIN_LINK)
        assert self.wait_for_url("login"), \
            "Navigation to Login page failed"
        assert "Login" in self.page_title(), \
            f"Expected 'Login' in page title, got: '{self.page_title()}'"

    def enter_email(self, value):
        self.type_text(*self.EMAIL, value)
        assert self.get_value(*self.EMAIL) == value, \
            f"Email input expected '{value}'"

    def enter_password(self, value):
        self.type_text(*self.PASSWORD, value)

    def submit_login(self):
        self.click(*self.LOGIN_BTN)

    def get_logged_in_user(self):
        """Get the logged-in account text shown in header."""
        if self.is_visible(*self.ACCOUNT_LINK, timeout=5):
            return self.get_text(*self.ACCOUNT_LINK)
        return ""

    def get_account_text(self):
        return self.get_text(*self.ACCOUNT_LINK)

    def login(self, email, password):
        self.go_to_login()

        assert self.is_visible(*self.EMAIL),     "Email field not visible"
        assert self.is_visible(*self.PASSWORD),  "Password field not visible"
        assert self.is_visible(*self.LOGIN_BTN), "Login button not visible"

        self.enter_email(email)
        self.enter_password(password)
        self.submit_login()

        assert self.is_logged_in(), \
            f"Login FAILED for '{email}' — account link not visible after submit"

        account_text = self.get_account_text()
        assert account_text, "Logged-in account display text is empty"
        assert email.lower() in account_text.lower(), \
            f"Logged-in account '{account_text}' does not match email '{email}'"

        assert "login" not in self.current_url().lower(), \
            f"Still on login page after successful login: {self.current_url()}"

        logger.info(f"Login successful. Account: '{account_text}'")
        return account_text

    def logout(self):
        if not self.is_logged_in():
            logger.warning("logout() called but no active session found — skipping")
            return

        parts = self.driver.current_url.split("/")
        base = parts[0] + "//" + parts[2]
        self.driver.get(f"{base}/logout")
        logger.info("Logout via direct /logout URL navigation")

    def verify_session_terminated(self, base_url):
        self.driver.get(f"{base_url}/customer/info")
        assert self.wait_for_url("login"), \
            f"Protected page did not redirect to login. URL: {self.current_url()}"
        logger.info("Session terminated — protected page redirected to login")