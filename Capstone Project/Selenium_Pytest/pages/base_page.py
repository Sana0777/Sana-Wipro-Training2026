import logging
import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

logger = logging.getLogger(__name__)


class BasePage:

    def __init__(self, driver, explicit_wait=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, explicit_wait)

    def find_element(self, by, locator):
        try:
            el = self.wait.until(EC.presence_of_element_located((by, locator)))
            logger.debug(f"Element found: ({by}, {locator})")
            return el
        except TimeoutException:
            logger.error(f"Element NOT found within timeout: ({by}, {locator})")
            raise

    def find_clickable(self, by, locator):
        try:
            el = self.wait.until(EC.element_to_be_clickable((by, locator)))
            return el
        except TimeoutException:
            logger.error(f"Element NOT clickable: ({by}, {locator})")
            raise

    def click(self, by, locator):
        self.find_clickable(by, locator).click()
        logger.info(f"Clicked: ({by}, {locator})")

    def type_text(self, by, locator, text):
        el = self.find_element(by, locator)
        el.clear()
        el.send_keys(text)
        logger.info(f"Typed '{text}' into ({by}, {locator})")

    def get_text(self, by, locator):
        text = self.find_element(by, locator).text
        logger.info(f"Text='{text}' from ({by}, {locator})")
        return text

    def get_value(self, by, locator):
        return self.find_element(by, locator).get_attribute("value")

    def is_visible(self, by, locator, timeout=8):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
            return True
        except TimeoutException:
            return False

    def is_present(self, by, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, locator))
            )
            return True
        except TimeoutException:
            return False

    def wait_for_url(self, partial, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_contains(partial))
            return True
        except TimeoutException:
            return False

    def current_url(self):
        return self.driver.current_url

    def page_title(self):
        return self.driver.title

    def scroll_into_view(self, by, locator):
        el = self.find_element(by, locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
        return el


    def take_screenshot(self, label="screenshot"):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        fname = f"{label}_{ts}.png"
        folder = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "screenshots"
        )
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, fname)
        self.driver.save_screenshot(path)
        logger.info(f"Screenshot saved → {path}")
        return path
