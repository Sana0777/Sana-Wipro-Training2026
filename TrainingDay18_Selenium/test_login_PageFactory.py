import time

from selenium import webdriver
from TrainingDay18_Selenium.login_page_PageFactory import Login_page_PageFactory


driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
loginobj = Login_page_PageFactory(driver)

loginobj.enter_username("Admin")
loginobj.enter_password("admin123")
loginobj.click_login()
print("Successfull")