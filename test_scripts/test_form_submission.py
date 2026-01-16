import pytest
import json
from faker import Faker
from conftest import init_driver
from test_pages.login_page import LoginPage
from test_pages.forms_page import CheckoutPage


@pytest.mark.usefixtures('init_driver')
class TestCheckout:
    def config_and_launch(self):
        try:
            with open('config.json', 'r') as file:
                config = json.load(file)
                print(config)

        except Exception as e:
            print("Exception occurred while reading the json file ", e)
        return config


    def test_launch(self):
        config = self.config_and_launch()
        url = config['url']
        self.url = CheckoutPage(self.driver)
        self.url.launch_url(url)


    def test_login_and_check(self):
        self.forms_page = CheckoutPage(self.driver)
        config = self.config_and_launch()
        username = config['username2']
        password = config['password']
        self.forms_page.user2_login(username,password)
        expected_title = config['title']
        actual_title = self.forms_page.loggedin_and_productsPg()
        assert actual_title==expected_title, f"User login issue, after successfully login expected title is {expected_title} but actual title is {actual_title}"


    def test_checkout(self):
        self.checkoutpg = CheckoutPage(self.driver)
        self.checkoutpg.products_added_to_cart()
        self.checkoutpg.click_checkout()

    def test_form_fill_and_submit(self):
        self.form = CheckoutPage(self.driver)
        fake_data = Faker()
        first_name = fake_data.first_name()
        last_name = fake_data.last_name()
        zip_code = fake_data.zipcode()
        self.form.fill_form(first_name, last_name,zip_code)
        print(f"To fill the form user details entered firstname: {first_name}, Lastname: {last_name} and zipcode: {zip_code}")


    def test_complete_checkout(self):
        self.finish_checkout = CheckoutPage(self.driver)
        assert self.finish_checkout.checkout(), "Products are not found"
        assert self.finish_checkout.checkout_and_finish(), "Unable to proceed with the products order process"



