from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class LabBookPage:
    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    desktops_menu = (By.LINK_TEXT, "Desktops")

    mac_link = (By.XPATH, "//a[contains(text(),'Mac')]")

    sort_dropdown = (By.ID, "input-sort")

    add_to_cart_btn = (By.XPATH, "//button[contains(@onclick,'cart.add')]")

    mac_heading = (By.XPATH, "//h2[text()='Mac']")

    search_box = (By.NAME, "search")

    search_btn = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")

    search_criteria = (By.ID, "input-search")

    desc_checkbox = (By.NAME, "description")

    search_again_btn = (By.ID, "button-search")

    def open_site(self):

        self.driver.get("https://tutorialsninja.com/demo/")
        self.driver.maximize_window()

    def open_mac_page(self):

        self.wait.until(
            EC.element_to_be_clickable(self.desktops_menu)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.mac_link)
        ).click()

    def sort_name_az(self):

        dropdown = self.wait.until(
            EC.presence_of_element_located(self.sort_dropdown)
        )

        Select(dropdown).select_by_visible_text("Name (A - Z)")

    def add_to_cart(self):

        self.wait.until(
            EC.element_to_be_clickable(self.add_to_cart_btn)
        ).click()

    def verify_mac_heading(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.mac_heading)
        ).is_displayed()

    def search_product(self, text):

        box = self.wait.until(
            EC.visibility_of_element_located(self.search_box)
        )

        box.clear()
        box.send_keys(text)

        self.driver.find_element(*self.search_btn).click()

    def clear_search(self):

        self.wait.until(
            EC.visibility_of_element_located(self.search_criteria)
        ).clear()

    def click_description(self):
        checkbox = self.wait.until(
            EC.element_to_be_clickable(self.desc_checkbox)
        )

        if not checkbox.is_selected():
            checkbox.click()

    def click_search_again(self):

        self.wait.until(
            EC.element_to_be_clickable(self.search_again_btn)
        ).click()
