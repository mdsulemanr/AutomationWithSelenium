# test_login.py
from selenium import webdriver
from pages.login_page import LoginPage


def test_valid_login():
    # Set up the WebDriver
    driver = webdriver.Chrome()

    # Create an instance of the LoginPage
    login_page = LoginPage(driver)

    # Perform the actions
    login_page.open_login_page()
    login_page.enter_username("tomsmith")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_login()

    # Verify the login by checking the success message
    success_message = login_page.get_success_message()
    assert "You logged into a secure area!" in success_message

    # Close the browser
    driver.quit()
