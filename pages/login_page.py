from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        #Locators for login
        self.email_input = (By.ID, "Email")
        self.password_input = (By.ID, "Password")
        self.login_button = (By.CSS_SELECTOR, "input.login-button")

    def open_login_page(self):
        self.driver.get("https://demowebshop.tricentis.com/login")

    def login(self, email, password):
        email_field = self.wait.until(EC.presence_of_element_located(self.email_input))
        email_field.clear()
        email_field.send_keys(email)

        password_field = self.driver.find_element(*self.password_input)
        password_field.clear()
        password_field.send_keys(password)

        login_btn = self.driver.find_element(*self.login_button)
        login_btn.click()
