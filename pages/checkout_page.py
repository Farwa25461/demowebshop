from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def continue_billing_address(self):
        #Continue with existing billing address
        continue_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#billing-buttons-container .new-address-next-step-button")
            )
        )
        continue_btn.click()

    def continue_shipping_address(self):
        #Continue with existing shipping address
        continue_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#shipping-buttons-container .new-address-next-step-button")
            )
        )
        continue_btn.click()

    def select_shipping_method(self):
        #Select In-store pickup and continue
        pickup_checkbox = self.wait.until(
            EC.element_to_be_clickable((By.ID, "PickUpInStore"))
        )
        if not pickup_checkbox.is_selected():
            pickup_checkbox.click()

        continue_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#shipping-method-buttons-container .shipping-method-next-step-button")
            )
        )
        continue_btn.click()

    def select_payment_method(self):
        #Select Cash on Delivery and continue
        continue_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#payment-method-buttons-container .payment-method-next-step-button")
            )
        )
        continue_btn.click()

    def continue_payment_info(self):
        #Continue without entering payment method
        continue_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#payment-info-buttons-container .payment-info-next-step-button")
            )
        )
        continue_btn.click()

    def confirm_order(self):
        #Click to confirm order
        confirm_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#confirm-order-buttons-container .confirm-order-next-step-button")
            )
        )
        confirm_btn.click()
