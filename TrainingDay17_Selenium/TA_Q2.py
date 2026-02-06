from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://letcode.in/alert")

driver.find_element(By.ID, "accept").click()

alert1 = wait.until(EC.alert_is_present())
print(alert1.text)
alert1.accept()

driver.find_element(By.ID, "confirm").click()

alert2 = wait.until(EC.alert_is_present())
print(alert2.text)
alert2.dismiss()

driver.find_element(By.ID, "prompt").click()

alert3 = wait.until(EC.alert_is_present())
alert3.send_keys("Sana")
alert3.accept()

result = driver.find_element(By.ID, "myName")

assert result.text == "Your name is: Sana"

print("All Alert Tests Passed")

driver.quit()
