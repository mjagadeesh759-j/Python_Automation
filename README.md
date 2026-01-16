# Python_Automation
This project contains automated test scripts for the web application using Selenium WebDriver with Python. The tests cover functionalities such as launching the application, user login, and more.

Project Structure:
test_scripts/ : Contains test case scripts.
test_pages/ : Contains Page Object Model classes for different pages.
Locators/ : Contains locators definitions for UI elements.
config.json : Configuration file with test data like URL, username, and password.
conftest.py : Pytest fixtures for WebDriver initialization and setup.
reports: To generate the html based test reports

Prerequisites:
Python 3.x installed
Install chrome/edge or any of the browser to execute the script 
e.g. ChromeDriver compatible with your Chrome version
Required Python packages installed (see Installation)

Clone the repository:
git clone <repository_url>
cd <repository_folder>

Install required packages:
pip install -r requirements.txt


Key features:
Page Object Model (POM) design pattern used
Configurable test data via config.json
Pytest fixtures for setup and teardown
Explicit waits for stable element interactions

Execute: 
Execute test scripts using pytest