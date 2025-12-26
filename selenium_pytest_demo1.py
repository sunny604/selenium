import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.implicitly_wait(10)
    # Yield the WebDriver instance
    yield driver
    #Close the WebDriver instance
    #driver.quit()


@pytest.mark.parametrize("username, password", [
    ("admin", "12345678")
    ("admin", "admin123"),
    ("user1", "password1"),  
])

def test_login(driver, username, password):
    driver.get("https://sandbox2.slurpit.io:2087/")
    username_field = driver.find_element(By.ID, value="sign_in_form_usr")
    password_field = driver.find_element(By.ID, value="sign_in_form_pwd")
    
    submit_button = driver.find_element(By.ID, value="kt_sign_in_submit")

    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()


    #input box
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.NAME, "fqdn")))
    element.click()


    