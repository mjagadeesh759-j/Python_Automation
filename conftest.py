import os
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
import pytest
from dotenv import load_dotenv
load_dotenv()

@pytest.fixture(scope='class')
def init_driver(request):
    browsers_list = ['chrome', 'edge', 'firefox','headless']
    browser = os.getenv('BROWSER', None)
    print("browser set in environment...",browser)

    if not browser:
        raise Exception("Environment variable 'BROWSER= ____ ' must be set to execute the script ")

    browser = browser.lower()
    if not browser in browsers_list:
        raise Exception(f"Provided browser{browser} is not in the supported browser list, please provide valid browser list {browsers_list}...")


    if browser == 'chrome':
        driver = webdriver.Chrome()

    elif browser == 'edge':
        driver = webdriver.Edge()

    elif browser == 'firefox':
        driver = webdriver.Edge()

    elif browser == 'headless':
        edge_options = EdgeOptions()
        edge_options.add_argument('--disable-gpu')
        edge_options.add_argument('--no-sandbox')
        edge_options.add_argument('--headless')
        edge_options.add_argument('window-size=1920,1080')
        driver = webdriver.Edge(options=edge_options)


    else:
        print(f"Invalid browser: {browser}")

    request.cls.driver = driver

    yield
    driver.quit()

