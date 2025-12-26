import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.firefox import GeckoDriverManager
from POMDemo.pages.login_page import LoginPage
import time

@pytest.fixture()
def driver():
    driver = webdriver.Firefox(
        executable_path=GeckoDriverManager().install()
    )
    driver.implicitly_wait(10)
    yield driver

@pytest.mark.parametrize(
    "username, password",
    [
        ("wronguser", "12345678"),
        ("admin", "12345678"),
    ]
)

def test_login(driver, username, password):
    login_page = LoginPage(driver)

    login_page.open_page("https://sandbox2.slurpit.io:2087/")
    time.sleep(1)

    login_page.enter_username(username=username)
    time.sleep(1)

    login_page.enter_password(password=password)
    time.sleep(1)

    login_page.click_login()

    #input box
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.NAME, "fqdn")))
    element.click()




    