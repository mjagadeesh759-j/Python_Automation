from operator import truediv

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.page_locators import LoginPageLocators, FormsPageLocators
from test_pages.login_page import LoginPage

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.home_page = LoginPageLocators.HOME_PAGE
        self.username = LoginPageLocators.LOGIN_USER_NAME
        self.password = LoginPageLocators.LOGIN_PASSWORD
        self.login_button = LoginPageLocators.LOGIN_BTN
        self.products_page = LoginPageLocators.PRODUCTS
        self.cart = LoginPageLocators.MY_CART_BTN
        self.checkout_page = FormsPageLocators.CHECKOUT_PG
        self.check_button = FormsPageLocators.CHECKOUT_BTN
        self.f_name = FormsPageLocators.F_NAME
        self.l_name = FormsPageLocators.L_NAME
        self.zcode= FormsPageLocators.PS_CODE
        self.continue_button = FormsPageLocators.CONTINUE_BTN
        self.payments = FormsPageLocators.PAYMENT_INFO
        self.total_cost = FormsPageLocators.TOTAL_INFO
        self.product1 = FormsPageLocators.PRODUCT1_IN_CART
        self.finish = FormsPageLocators.FINISH_BTN
        self.thanks_msg = FormsPageLocators.SUCCESS_MSG


    def launch_url(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def user2_login(self,username,password):
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

    def loggedin_and_productsPg(self):
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located(self.products_page))
            actual_title = self.driver.current_url
            return actual_title


    def products_added_to_cart(self):
        product_bag = self.driver.find_element(*self.product1)
        product_bag.click()
        print("products added successfully ")


    def click_checkout(self):
        my_cart = self.driver.find_element(*self.cart)
        my_cart.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.checkout_page))
        # self.driver.find_element(*self.check_button).click()
        # self.driver.find_element(*self.checkout_page)
        self.driver.find_element(*self.check_button).click()

    def fill_form(self, fname, lname, z_ipcode):
        first_name = self.driver.find_element(*self.f_name)
        first_name.clear()
        first_name.send_keys(fname)
        last_name = self.driver.find_element(*self.l_name)
        last_name.clear()
        last_name.send_keys(lname)
        zip_code =self.driver.find_element(*self.zcode)
        zip_code.clear()
        zip_code.send_keys(z_ipcode)
        continue_button = self.driver.find_element(*self.continue_button)
        continue_button.click()


    def checkout(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located(self.payments))
            self.driver.find_element(*self.total_cost)
            return True
        except:
            return False

    def checkout_and_finish(self):
        try:
            finish = self.driver.find_element(*self.finish)
            wait = WebDriverWait(self.driver, 10)
            if wait.until(EC.element_to_be_clickable(self.finish)):
                # self.driver.execute_script("arguments[0].click();", finish)
                finish.click()
                print("finish button clicked...")
            else:
                raise Exception("Finish button is not enabled to interact...")
            return True
        except:
            raise Exception("Error occurred when finish and checkout...")

