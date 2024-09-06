import logging
import logging.config
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# logging.config.fileConfig('logging.conf')
# logger = logging.getLogger(__name__)

# Configure logging
logging.basicConfig(
    filename='test_log.log',  # Set log file name
    filemode='a',  # Append to file
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


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
            logging.error(f"Element {locator} not found.")
            return None

    # Actions
    def open_login_page(self, url):
        """Opens the login page."""
        logging.info(f"Opening login page: {url}")
        self.driver.get(url)

    def enter_username(self, username):
        """Fills the username field with error handling."""
        element = self.find_element(self.username_field)
        if element:
            element.send_keys(username)
            logging.info("Entered username.")
        else:
            logging.error("Username field not found.")

    def enter_password(self, password):
        """Fills the password field with error handling."""
        element = self.find_element(self.password_field)
        if element:
            element.send_keys(password)
            logging.info("Entered password.")
        else:
            logging.error("Password field not found.")

    def click_login(self):
        """Clicks the login button with error handling."""
        element = self.find_element(self.login_button)
        if element:
            element.click()
            logging.info("Clicked login button.")
        else:
            logging.error("Login button not found.")

    # Getter
    def get_success_message(self):
        """Gets the success message after login with error handling."""
        element = self.find_element(self.success_message)
        if element:
            success_message = element.text
            logging.info("Success message retrieved.")
            return success_message
        else:
            logging.error("Success message not found.")
            return None
