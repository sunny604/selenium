import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()

username1 = "Incorrect"
password1 = "Incorrect"

username2 = "admin"
password2 = "Incorrect"

username3 = "Incorrect"
password3 = "12345678"

username4 = "admin"
password4 = "12345678"

login_url = "https://sandbox2.slurpit.io:2087/"

driver.get(login_url)

# check whether the login button is enabled or not 
#login_button = driver.find_element(By.ID, value="kt_sign_in_submit")
#assert not login_button.get_attribute("disabled")
#login_button.click()

username_field1 = driver.find_element(By.ID, value="sign_in_form_usr")
password_field1 = driver.find_element(By.ID, value="sign_in_form_pwd")

#scenerio 1 : 
username_field1.send_keys(username1)
password_field1.send_keys(password1)

login_button1 = driver.find_element(By.ID, value="kt_sign_in_submit")
login_button1.click()

message = "scenerio 1 failed"
print(message)

driver.refresh()

#scenerio 2 : 
username_field2 = driver.find_element(By.ID, value="sign_in_form_usr")
password_field2 = driver.find_element(By.ID, value="sign_in_form_pwd")

username_field2.send_keys(username2)
password_field2.send_keys(password2)

login_button2 = driver.find_element(By.ID, value="kt_sign_in_submit")
login_button2.click()

message = "scenerio 2 failed"
print(message)

driver.refresh()

#scenerio 3 : 
username_field3 = driver.find_element(By.ID, value="sign_in_form_usr")
password_field3 = driver.find_element(By.ID, value="sign_in_form_pwd")
username_field3.send_keys(username3)
password_field3.send_keys(password3)

login_button3 = driver.find_element(By.ID, value="kt_sign_in_submit")
login_button3.click()

message = "scenerio 3 failed"
print(message)

driver.refresh()

#scenerio4(valid username, invalid password) 1 
username_field4 = driver.find_element(By.ID, value="sign_in_form_usr")
password_field4 = driver.find_element(By.ID, value="sign_in_form_pwd")
username_field4.send_keys(username4)
password_field4.send_keys(password4)

login_button4 = driver.find_element(By.ID, value="kt_sign_in_submit")
start_time = time.time()

login_button4.click()

#input box
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.NAME, "fqdn")))
element.click()

end_time = time.time()
page_load_time = end_time - start_time
print("Page load time:", page_load_time, "seconds")

message = "scenerio 4 : Passed"
print(message)





















