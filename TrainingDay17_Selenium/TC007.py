from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://artoftesting.com/samplesiteforselenium")

time.sleep(3)

driver.find_element(By.ID, "ConfirmBox").click()

print("Clicked Confirm Box. Waiting 5 seconds...")

time.sleep(5)

driver.quit()
