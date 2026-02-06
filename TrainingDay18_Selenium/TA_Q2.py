import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

print("Opening iframe demo page...")

driver.get("https://the-internet.herokuapp.com/iframe")

time.sleep(3)

driver.switch_to.frame("mce_0_ifr")
text_box = driver.find_element(By.ID, "tinymce")
text_box.send_keys(Keys.CONTROL + "a")
text_box.send_keys(Keys.DELETE)

text_box.send_keys("Hello !")

print("Text entered inside iframe")

time.sleep(2)

driver.switch_to.default_content()

print("Switched back to main page")

time.sleep(2)


print("Opening new tab...")

driver.execute_script("window.open('https://www.google.com','_blank');")

time.sleep(2)

windows = driver.window_handles
parent_window = driver.current_window_handle

for window in windows:
    if window != parent_window:

        driver.switch_to.window(window)
        print("\nClosing child window : Title :", driver.title)

        driver.close()
        time.sleep(1)

driver.switch_to.window(parent_window)

print("\nBack to Parent window : Title :", driver.title)

time.sleep(3)

driver.quit()

print("\nTest Completed Successfully")
