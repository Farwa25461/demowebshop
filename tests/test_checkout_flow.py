import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def driver():
    #Setting up browser then tearing down when process complete
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.quit()


def test_full_checkout_flow(driver):

    #Loggin in using my credentials i have created manually
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login("farwaramzann734@gmail.com", "1234567")

    #Searching for computer and adding add to cart
    product_page = ProductPage(driver)
    product_page.search_and_add_product("Computer")

    #Go to cart after closing top snackbar message
    cart_page = CartPage(driver)
    cart_page.accept_terms_and_checkout()

    #Proceeding with order and giving test data
    checkout_page = CheckoutPage(driver)
    checkout_page.continue_billing_address()
    checkout_page.continue_shipping_address()
    checkout_page.select_shipping_method()
    checkout_page.select_payment_method()
    checkout_page.continue_payment_info()
    checkout_page.confirm_order()

    #Veryfying order
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    confirmation_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".section.order-completed"))
    ).text

    assert "Your order has been successfully processed" in confirmation_message
