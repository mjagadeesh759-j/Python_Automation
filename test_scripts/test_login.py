import pytest
import json
from conftest import init_driver
from test_pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('init_driver')
class Testloginprocess:
    def config_data(self):
        try:
            with open('config.json', 'r') as file:
                config = json.load(file)
                print(config)

        except Exception as e:
            print("Exception occurred while reading the json file ", e)
        return config

    # @pytest.fixture(scope="function")
    # def test_check(self):
    #     self.login_pg = LoginPage(self.driver)


    def test_launch(self):
        config = self.config_data()
        url = config['url']
        self.url = LoginPage(self.driver)
        self.url.launch_url(url)

    def test_login(self):
        self.login_page = LoginPage(self.driver)
        config = self.config_data()
        username = config['username1']
        password = config['password']
        self.login_page.user_login(username,password)
        expected_title = config['title']
        actual_title = self.login_page.loggedin_and_ProductsPg()
        assert actual_title==expected_title, f"User login issue, after successfully login expected title is {expected_title} but actual title is {actual_title}"


    def test_add_cart(self):
        self.cartpg = LoginPage(self.driver)
        products = self.cartpg.products_added_to_cart()
        print(f"Produces are successfully added to the cat and products are {products}_displaying in my carts")



