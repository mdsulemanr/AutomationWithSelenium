from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPage:
    # Locators as class variables
    username_field = (By.ID, "username")
    password_field = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button.radius")
    success_message = (By.CSS_SELECTOR, "div.flash.success")

    def __init__(self, driver):
        self.driver = driver

    # Centralized method for finding elements with error handling
    def find_element(self, locator):
        """Helper method to find an element with error handling."""
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            print(f"Element {locator} not found.")
            return None

    # Actions
    def open_login_page(self, url):
        """Opens the login page."""
        self.driver.get(url)

    def enter_username(self, username):
        """Fills the username field with error handling."""
        element = self.find_element(self.username_field)
        if element:
            element.send_keys(username)
        else:
            print("Username field not found.")

    def enter_password(self, password):
        """Fills the password field with error handling."""
        element = self.find_element(self.password_field)
        if element:
            element.send_keys(password)
        else:
            print("Password field not found.")

    def click_login(self):
        """Clicks the login button with error handling."""
        element = self.find_element(self.login_button)
        if element:
            element.click()
        else:
            print("Login button not found.")

    # Getter
    def get_success_message(self):
        """Gets the success message after login with error handling."""
        element = self.find_element(self.success_message)
        if element:
            return element.text
        else:
            print("Success message not found.")
            return None
