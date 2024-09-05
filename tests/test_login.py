from selenium import webdriver
from pages.login_page import LoginPage

def test_valid_login():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    # Open the login page
    login_page.open_login_page()

    # Perform login actions
    login_page.enter_username("tomsmith")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_login()

    # Verify the success message
    success_message = login_page.get_success_message()
    assert "You logged into a secure area!" in success_message

    # Close the browser
    driver.quit()
