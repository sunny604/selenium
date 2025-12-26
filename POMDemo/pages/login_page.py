from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "sign_in_form_usr")
        self.password_textbox = (By.ID, "sign_in_form_pwd")
        self.login_button = (By.ID, "kt_sign_in_submit")

#Test
    def open_page(self, url):
        self.driver.get(url)
    
    # login_page.py
    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

