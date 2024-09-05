from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button.radius")
        self.success_message = (By.CSS_SELECTOR, "div.flash.success")

    def open_login_page(self):
        """Opens the login page."""
        self.driver.get("https://the-internet.herokuapp.com/login")

    def find_element(self, locator):
        """Helper method to find elements with error handling."""
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            print(f"Element {locator} not found.")
            return None

    def enter_username(self, username):
        """Enters the username in the username field."""
        element = self.find_element(self.username_field)
        if element:
            element.send_keys(username)

    def enter_password(self, password):
        """Enters the password in the password field."""
        element = self.find_element(self.password_field)
        if element:
            element.send_keys(password)

    def click_login(self):
        """Clicks the login button."""
        element = self.find_element(self.login_button)
        if element:
            element.click()

    def get_success_message(self):
        """Returns the success message after login."""
        element = self.find_element(self.success_message)
        return element.text if element else ""
