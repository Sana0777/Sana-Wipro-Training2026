from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://letcode.in/window")

driver.find_element(By.ID,"multi").click()

window=driver.window_handles

for child in window:
    driver.switch_to.window(child)
    print("Current URL:",driver.current_url)

driver.quit()