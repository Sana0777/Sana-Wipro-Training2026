from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
time.sleep(3)

driver.find_element(By.LINK_TEXT,"Desktops").click()
driver.find_element(By.LINK_TEXT,"Mac (1)").click()
dropdown=Select(driver.find_element(By.ID,"input-sort"))
options=dropdown.options
for option in options:
    print(option.text)
dropdown.select_by_index(4)
driver.quit()