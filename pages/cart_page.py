from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 12)

        #Locators for cart
        self.terms_checkbox = (By.ID, "termsofservice")
        self.checkout_button = (By.ID, "checkout")

    def accept_terms_and_checkout(self):

        checkbox = self.wait.until(EC.element_to_be_clickable(self.terms_checkbox))
        checkbox.click()

        checkout_btn = self.wait.until(EC.element_to_be_clickable(self.checkout_button))
        checkout_btn.click()
