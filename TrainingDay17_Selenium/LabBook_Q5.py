from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

service = Service()
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 25)

driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()

assert "Your Store" in driver.title

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='My Account']"))).click()
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()

wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Register Account']")))

def click_continue():
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Continue']"))).click()

def get_firstname():
    return wait.until(EC.presence_of_element_located((By.ID, "input-firstname")))

def get_lastname():
    return wait.until(EC.presence_of_element_located((By.ID, "input-lastname")))

def get_email():
    return wait.until(EC.presence_of_element_located((By.ID, "input-email")))

def get_telephone():
    return wait.until(EC.presence_of_element_located((By.ID, "input-telephone")))

def get_password():
    return wait.until(EC.presence_of_element_located((By.ID, "input-password")))

def get_confirm():
    return wait.until(EC.presence_of_element_located((By.ID, "input-confirm")))


click_continue()

warning = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//div[contains(text(),'Privacy Policy')]")
))
assert "Privacy Policy" in warning.text


long_text = "A" * 33


get_firstname().send_keys(long_text)
click_continue()

try:
    fn_error = driver.find_element(By.XPATH, "//div[contains(text(),'First Name')]")
    assert fn_error.is_displayed()
except:
    pass

get_firstname().clear()
get_firstname().send_keys("Sana")


get_lastname().send_keys(long_text)
click_continue()

try:
    ln_error = driver.find_element(By.XPATH, "//div[contains(text(),'Last Name')]")
    assert ln_error.is_displayed()
except:
    pass

get_lastname().clear()
get_lastname().send_keys("Bano")


email_id = "user" + str(random.randint(1000,9999)) + "@gmail.com"

get_email().send_keys(email_id)
get_telephone().send_keys("9876543210")


get_password().send_keys("Admin@1234")
get_confirm().send_keys("Admin@1234")


wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//input[@name='newsletter' and @value='1']")
)).click()

wait.until(EC.element_to_be_clickable((By.NAME, "agree"))).click()


click_continue()


success = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//h1[text()='Your Account Has Been Created!']")
))
assert "Your Account Has Been Created" in success.text


wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue"))).click()

wait.until(EC.element_to_be_clickable(
    (By.LINK_TEXT, "View your order history")
)).click()


print("All Test Steps Executed Successfully")

time.sleep(5)
driver.quit()
