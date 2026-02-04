from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_A():
    driver = webdriver.Chrome()

    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    time.sleep(2)

    print("title is :",driver.title)

    driver.get("https://www.google.com")
    driver.forward()
    print("title :",driver.title )
    driver.back()
    print("after title :",driver.title )
    driver.quit()