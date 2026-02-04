from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_register():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

    time.sleep(2)

    driver.find_element(By.ID, "input-firstname").send_keys("Sana")

    driver.find_element(By.NAME, "lastname").send_keys("Bano")

    driver.find_element(By.CSS_SELECTOR, "#input-email").send_keys("Sana08877@gmail.com")

    driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys("1234567890")

    driver.find_element(By.ID, "input-password").send_keys("admin123")

    driver.find_element(By.ID, "input-confirm").send_keys("admin123")

    driver.find_element(By.CSS_SELECTOR,
        "input[name='newsletter'][value='1']").click()

    driver.find_element(By.NAME, "agree").click()

    driver.find_element(By.XPATH, "//input[@value='Continue']").click()

    time.sleep(3)

    msg = driver.find_element(
        By.XPATH, "//h1[contains(text(),'Your Account Has Been Created')]"
    ).text
    assert "Your Account Has Been Created" in msg
    driver.quit()
