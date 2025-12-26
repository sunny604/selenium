from selenium import webdriver     

# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded.
import time 
 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

# Creating an instance webdriver
browser = webdriver.Firefox() 
browser.get('https://twitter.com/')

# Let's the user see and also load the element 
time.sleep(2)
 
login = browser.find_elements(By.XPATH, '//*[@id=&quot;doc&quot;]/div[1]/div/div[1]/div[2]/a[3]')

# using the click function which is similar to a click in the mouse.
login[0].click()

user = browser.find_elements(By.XPATH, '//*[@id=&quot;login-dialog-dialog&quot;]/div[2]/div[2]/div[2]/form/div[1]/input')

# Enter User Name
user[0].send_keys('USER-NAME')

user = browser.find_element(By.XPATH, '//*[@id=&quot;login-dialog-dialog&quot;]/div[2]/div[2]/div[2]/form/div[2]/input')

# Reads password from a text file because
# saving the password in a script is just silly.
with open('test.txt', 'r') as myfile:  
    Password = myfile.read().replace('\n', '')
user.send_keys(Password)

LOG = browser.find_elements(By.XPATH, '//*[@id=&quot;login-dialog-dialog&quot;]/div[2]/div[2]/div[2]/form/input[1]')
LOG[0].click()

time.sleep(5)

elem = browser.find_element(By.XPATH, &quot;q&quot;)
elem.click()
elem.clear()

elem.send_keys(&quot;Geeks for geeks &quot;)

# using keys to send special KEYS 
elem.send_keys(Keys.RETURN) 

print(&quot;Search Successful&quot;)

# closing the browser
browser.close()