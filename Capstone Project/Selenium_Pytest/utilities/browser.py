import configparser
import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

logger = logging.getLogger(__name__)

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "config.ini")

config = configparser.ConfigParser()
config.read(CONFIG_PATH)


def get_base_url():
    return config.get("settings", "base_url")


def get_driver():
    browser = config.get("settings", "browser", fallback="chrome").lower()

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--allow-insecure-localhost")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.set_capability("acceptInsecureCerts", True)
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.set_capability("acceptInsecureCerts", True)
        driver = webdriver.Firefox(options=options)

    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--no-first-run")
        options.add_argument("--no-default-browser-check")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.set_capability("acceptInsecureCerts", True)
        driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    logger.info(f"WebDriver started: {browser}")
    return driver