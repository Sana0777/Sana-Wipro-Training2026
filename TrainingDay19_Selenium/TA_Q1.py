from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

driver.implicitly_wait(10)
print("Implicit wait set to 10 seconds")

driver.find_element(By.XPATH, "//button[text()='Enable']").click()

try:
    explicit_wait = WebDriverWait(driver, 10)
    textbox = explicit_wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))
    )
    print("Explicit wait: Element is clickable")
except TimeoutException:
    print("Explicit wait: Element not clickable")

try:
    fluent_wait = WebDriverWait(
        driver,
        timeout=10,
        poll_frequency=2,
        ignored_exceptions=[NoSuchElementException]
    )

    element = fluent_wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))
    )

    print("Fluent wait: Element available")

except TimeoutException:
    print("Fluent wait: Element not found")

element.send_keys("Working")

time.sleep(3)
driver.quit()
