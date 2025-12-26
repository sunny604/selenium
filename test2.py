from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# create webdriver object
driver = webdriver.Firefox()

# Chrome options
options = Options()
options.add_argument("--start-maximized")

try:
    # Navigate to the website
    driver.get("https://www.geeksforgeeks.org/")

    # Get all cookies
    print("Initial cookies:", driver.get_cookies())

    # Add a cookie
    driver.add_cookie({'name': 'foo', 'value': 'bar'})
    print("After adding 'foo':", driver.get_cookies())

    # Delete the cookie
    driver.delete_cookie("foo")
    print("After deleting 'foo':", driver.get_cookies())

    # Verify deletion
    if driver.get_cookie("foo") is None:
        print("Cookie 'foo' successfully deleted!")
    else:
        print("Cookie 'foo' still exists!")

finally:
    driver.quit()



