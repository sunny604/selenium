# Python program to demonstrate selenium
# import webdriver
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

# create webdriver object
driver = webdriver.Firefox()

# Navigate to the webpage (Ensure the URL is correct without spaces)
driver.get("https://www.geeksforgeeks.org/")

# Wait for the alert to appear (you might need to adjust the time based on your page load time)
time.sleep(3)

# Switch to the alert
alert = Alert(driver)

# Get the alert text
print(alert.text)

# Accept the alert
alert.accept()

# Close the browser
driver.quit()








