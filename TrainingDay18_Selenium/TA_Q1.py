import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Config:
    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USERNAME = "Admin"
    PASSWORD = "admin123"


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def type_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_element(self, locator):
        return self.driver.find_element(*locator)


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    loginbutton = (By.XPATH, "//button[@type='submit']")
    dashboard = (By.XPATH, "//h6[text()='Dashboard']")

    def enter_username(self, user):
        self.type_text(self.username, user)

    def enter_password(self, pwd):
        self.type_text(self.password, pwd)

    def click_login(self):
        self.click(self.loginbutton)

    def is_login_success(self):
        return self.get_element(self.dashboard).is_displayed()


@pytest.fixture(scope="class")
def setup(request):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get(Config.BASE_URL)

    request.cls.driver = driver

    yield

    time.sleep(2)
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_valid_login(self):

        loginobj = LoginPage(self.driver)

        loginobj.enter_username(Config.USERNAME)
        loginobj.enter_password(Config.PASSWORD)
        loginobj.click_login()

        time.sleep(3)

        result = loginobj.is_login_success()

        print("Login Successful:", result)

        assert result == True


