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

def test_google_search():
    # Initialize Firefox driver
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install()) 

    driver.implicitly_wait(10)
    driver.get("https://google.com")
    
    # Locate search box and enter query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)
    
    # Optional: wait until results appear
    WebDriverWait(driver, 10).until(EC.title_contains("Selenium"))
    
    print("Test Completed")
    
   

