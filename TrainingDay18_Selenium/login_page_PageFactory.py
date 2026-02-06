from selenium.webdriver.common.by import By

class Login_page_PageFactory:

    def __init__(self, driver):
        self.driver = driver

    @property
    def username(self):
        return self.driver.find_element(By.NAME, "username")

    @property
    def password(self):
        return self.driver.find_element(By.NAME, "password")

    @property
    def loginbutton(self):
        return self.driver.find_element(By.XPATH, "//button[@type='submit']")


    def enter_username(self, user):
        self.username.send_keys(user)

    def enter_password(self, pwd):
        self.password.send_keys(pwd)

    def click_login(self):
        self.loginbutton.click()
