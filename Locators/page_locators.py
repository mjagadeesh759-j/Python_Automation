from selenium.webdriver.common.by import By

class LoginPageLocators:
    HOME_PAGE = (By.XPATH, "//div[contains(text(), 'Swag Labs')]")
    LOGIN_USER_NAME = (By.ID, "user-name")
    LOGIN_PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    PRODUCTS = (By.ID, "inventory_container")
    CART1 = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART2 = (By.ID, "add-to-cart-sauce-labs-bike-light")
    MY_CART_BTN = (By.CLASS_NAME, "shopping_cart_link")
    PRODUCT1_IN_CART = (By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]")
    PRODUCT2_IN_CART = (By.XPATH, "//div[contains(text(),'Sauce Labs Bike Light')]")
    CART_LIST = (By.CLASS_NAME, "cart_list")



class  FormsPageLocators:
    PRODUCT1_IN_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    MY_CART = (By.ID, "shopping_cart_container")
    CHECKOUT_BTN = (By.ID, "checkout")
    CHECKOUT_PG = (By.XPATH, "//span[contains(text(), 'Your Cart')]")
    F_NAME = (By.ID, "first-name")
    L_NAME = (By.ID, "last-name")
    PS_CODE = (By.ID, "postal-code")
    CANCEL_BTN = (By.ID, "cancel")
    CONTINUE_BTN = (By.ID, "continue")
    CART_LIST = (By.CLASS_NAME, "cart_list")
    PAYMENT_INFO = (By.XPATH, '//div[@data-test="payment-info-label"]//following-sibling::div[@data-test="payment-info-value"]')
    SHIPPING_INFO = (By.XPATH, '//div[@data-test="shipping-info-label"]')
    TOTAL_INFO = (By.XPATH, '//div[@data-test="shipping-info-label"]')
    FINISH_BTN = (By.ID, "finish")
    SUCCESS_MSG = (By.XPATH, "//h2[contains(text(),'Thank you for your order!')]")

