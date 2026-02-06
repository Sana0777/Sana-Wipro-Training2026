from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.amazon.in")

driver.execute_script("alert('Hello Amazon')")
alert = driver.switch_to.alert
time.sleep(3)
alert.accept()

driver.execute_script("window.scrollBy(0,900)")
time.sleep(5)

print("Successful")
driver.quit()
