import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        #Locators for addig product
        self.search_box = (By.ID, "small-searchterms")
        self.search_button = (By.CSS_SELECTOR, "input[type='submit'][value='Search']")
        self.first_product = (By.CSS_SELECTOR, "h2.product-title a")
        self.add_to_cart_button = (By.CSS_SELECTOR, "input[value='Add to cart']")
        self.cart_icon = (By.CSS_SELECTOR, "a.ico-cart")
        self.notification_bar = (By.ID, "bar-notification")

    def search_and_add_product(self, product_name):

        search_input = self.wait.until(EC.visibility_of_element_located(self.search_box))
        search_input.clear()
        search_input.send_keys(product_name)

        try:
            search_btn = self.wait.until(EC.element_to_be_clickable(self.search_button))
            search_btn.click()
        except Exception:
            search_input.send_keys("\n")

        first_prod = self.wait.until(EC.element_to_be_clickable(self.first_product))
        first_prod.click()

        add_cart_btn = self.wait.until(EC.element_to_be_clickable(self.add_to_cart_button))
        add_cart_btn.click()

        try:
            self.wait.until(EC.visibility_of_element_located(self.notification_bar))
            self.wait.until(EC.invisibility_of_element_located(self.notification_bar))
        except Exception:

            #Waiting for snackbar message gone
            time.sleep(1)

        #Click cart icon
        cart = self.wait.until(EC.element_to_be_clickable(self.cart_icon))
        cart.click()
