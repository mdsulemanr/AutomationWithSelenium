from selenium import webdriver
from pages.login_page import LoginPage
from config import BASE_URL, USERNAME, PASSWORD


def test_valid_login():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    # Open the login page using the base URL from config
    login_page.open_login_page(BASE_URL)

    # Perform login actions using constants for username and password
    login_page.enter_username(USERNAME)
    login_page.enter_password(PASSWORD)
    login_page.click_login()

    # Verify the success message
    success_message = login_page.get_success_message()
    assert "You logged into a secure area!" in success_message
    driver.save_screenshot("login_page.png")

    # Close the browser
    driver.quit()
