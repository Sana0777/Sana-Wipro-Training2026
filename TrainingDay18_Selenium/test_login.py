import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from login_page import LoginPage

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

loginobj = LoginPage(driver)

loginobj.enter_username("Admin")
loginobj.enter_password("admin123")
loginobj.click_login()
