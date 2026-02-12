from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import pytest
GRIDURL ="http://10.202.252.183:4444/wd/hub"


def get_driver(browser):
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")

    elif browser == "firefox":
        options = FirefoxOptions()

    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")

    else:
        raise ValueError("Browser not supported")

    driver = webdriver.Remote(
        command_executor=GRIDURL,
        options=options
    )

    driver.maximize_window()
    return driver

@pytest.mark.parametrize("browser", ["chrome", "firefox", "edge"])
def test_page_title(browser):
    driver = get_driver(browser)

    driver.get("https://www.google.com")

    assert "Google" in driver.title

    capabilities = driver.capabilities
    print(
        f"Browser : {capabilities.get('browserName')}, "
        f"Platform : {capabilities.get('platformName')}"
    )

    driver.quit()