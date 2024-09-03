from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium import webdriver

# Set up the WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Print the title of the page
print(driver.title)

# Close the browser
driver.quit()
