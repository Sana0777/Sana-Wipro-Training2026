from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://artoftesting.com/samplesiteforselenium")

driver.find_element(By.ID, "fname").send_keys("Sana")

driver.find_element(By.ID, "female").click()

driver.find_element(By.CLASS_NAME, "Automation").click()
driver.find_element(By.CLASS_NAME, "Performance").click()

dropdown = Select(driver.find_element(By.ID, "testingDropdown"))
dropdown.select_by_visible_text("Database Testing")

driver.find_element(By.ID, "ConfirmBox").click()

alert = wait.until(EC.alert_is_present())
alert.accept()

result = driver.find_element(By.ID, "demo")

assert result.text == "You pressed OK!"

print("Test Passed")

driver.quit()
