import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class RegistrationPage(BasePage):

    REGISTER_LINK          = (By.XPATH,       "//a[text()='Register']")
    GENDER_MALE_RADIO      = (By.ID,          "gender-male")
    GENDER_FEMALE_RADIO    = (By.ID,          "gender-female")
    FIRST_NAME_INPUT       = (By.ID,          "FirstName")
    LAST_NAME_INPUT        = (By.ID,          "LastName")
    EMAIL_INPUT            = (By.ID,          "Email")
    PASSWORD_INPUT         = (By.ID,          "Password")
    CONFIRM_PASSWORD_INPUT = (By.ID,          "ConfirmPassword")
    REGISTER_BUTTON        = (By.ID,          "register-button")
    REGISTRATION_RESULT    = (By.CLASS_NAME,  "result")
    EMAIL_ERROR            = (By.CSS_SELECTOR,"#Email-error, .field-validation-error")

    def register(self, first_name, last_name, email, password, gender):
        logger.info(f"Attempting registration for {email}")

        self.click(*self.REGISTER_LINK)

        if gender.lower() == "female":
            self.click(*self.GENDER_FEMALE_RADIO)
        else:
            self.click(*self.GENDER_MALE_RADIO)

        self.type_text(*self.FIRST_NAME_INPUT,       first_name)
        self.type_text(*self.LAST_NAME_INPUT,        last_name)
        self.type_text(*self.EMAIL_INPUT,            email)
        self.type_text(*self.PASSWORD_INPUT,         password)
        self.type_text(*self.CONFIRM_PASSWORD_INPUT, password)

        self.click(*self.REGISTER_BUTTON)


        try:
            WebDriverWait(self.driver, 8).until(
                lambda d: (
                    "registerresult" in d.current_url.lower()
                    or "register" not in d.current_url.lower()
                    or any(phrase in d.page_source.lower() for phrase in [
                        "already exist", "already registered",
                        "email is already", "the specified email already exists",
                    ])
                )
            )
        except Exception:
            pass  # fall through to detection logic below

        page_source = self.driver.page_source.lower()
        current_url = self.driver.current_url.lower()

        ALREADY_REGISTERED_PHRASES = [
            "already exist",
            "already registered",
            "email is already",
            "username is already",
            "the specified email already exists",
        ]

        if any(phrase in page_source for phrase in ALREADY_REGISTERED_PHRASES):
            logger.warning(f"Email already registered: {email} — skipping to login")
            return "already_exists"

        if "registerresult" in current_url or "your registration completed" in page_source:
            logger.info(f"Registration successful for {email}")
            return "registered"

        if "register" not in current_url:
            logger.info(f"Registration redirected to {current_url} — treating as success")
            return "registered"

        try:
            result_el = self.driver.find_element(*self.REGISTRATION_RESULT)
            result_text = result_el.text.strip()
            if result_text:
                if any(phrase in result_text.lower() for phrase in ALREADY_REGISTERED_PHRASES):
                    logger.warning(f"Already registered (result element): {email}")
                    return "already_exists"
                logger.info(f"Registration result: {result_text}")
                return "registered"
        except Exception:
            pass

        raise AssertionError(
            f"Registration failed unexpectedly for {email}.\n"
            f"URL: {self.driver.current_url}\n"
            f"Page snippet: {self.driver.page_source[2000:3000]}"
        )