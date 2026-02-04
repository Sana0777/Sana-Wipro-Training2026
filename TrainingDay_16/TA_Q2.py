from selenium import webdriver
import time

def test_browser_navigation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(2)

    print("Page Title :", driver.title)

    driver.find_element("xpath", "//a").click()
    time.sleep(2)
    print("Page Title :", driver.title)

    driver.back()
    time.sleep(2)
    print("After Back :", driver.title)

    driver.forward()
    time.sleep(2)
    print("After Forward :", driver.title)

    driver.refresh()
    time.sleep(2)
    print("After Refresh :", driver.title)
    driver.quit()
