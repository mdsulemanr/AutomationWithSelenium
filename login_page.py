from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver
driver = webdriver.Chrome()

# Open the login page
driver.get("https://the-internet.herokuapp.com/login")

# Find the username field and enter a username
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

# Find the password field and enter a password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

# Find the login button and click it
login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()

# Verify the login by checking the URL or looking for a logout button
success_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success").text
assert "You logged into a secure area!" in success_message

# Close the browser
driver.quit()
