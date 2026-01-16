from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.page_locators import LoginPageLocators

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.home_page = LoginPageLocators.HOME_PAGE
        self.username = LoginPageLocators.LOGIN_USER_NAME
        self.password = LoginPageLocators.LOGIN_PASSWORD
        self.login_button = LoginPageLocators.LOGIN_BTN
        self.products_page = LoginPageLocators.PRODUCTS
        self.product1 = LoginPageLocators.CART1
        self.product2 = LoginPageLocators.CART2
        self.cart = LoginPageLocators.MY_CART_BTN
        self.prod1_order = LoginPageLocators.PRODUCT1_IN_CART
        self.prod2_order = LoginPageLocators.PRODUCT2_IN_CART
        self.cartlist = LoginPageLocators.CART_LIST

    def launch_url(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def user_login(self, username,password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.home_page))
        user_name = self.driver.find_element(*self.username)
        user_name.clear()
        user_name.send_keys(username)
        pass_word =self.driver.find_element(*self.password)
        pass_word.clear()
        pass_word.send_keys(password)
        login_button = self.driver.find_element(*self.login_button)
        login_button.click()

    def loggedin_and_ProductsPg(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located(self.products_page))
            actual_title = self.driver.current_url
            return actual_title

    def products_added_to_cart(self):
        product_bag = self.driver.find_element(*self.product1)
        product_bag.click()
        product_light = self.driver.find_element(*self.product2)
        product_light.click()
        mycart = self.driver.find_element(*self.cart)
        mycart.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.cartlist))
        bag = self.driver.find_element(*self.prod1_order)
        light = self.driver.find_element(*self.prod2_order)
        bags = bag.text
        lights = light.text
        return bags, lights

