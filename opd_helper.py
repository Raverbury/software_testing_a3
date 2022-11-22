from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector
import requests
from _test_config import TestConfig


class Client():

    @staticmethod
    def get_signup_button(driver: WebDriver):
        buttons = driver.find_elements(By.TAG_NAME, "button")
        sign_up_button = list(
            filter(lambda x: x.get_attribute("innerHTML") == "SignUp", buttons))[0]
        return sign_up_button

    @staticmethod
    def get_signup_form_submit_button(driver: WebDriver):
        forms = driver.find_elements(By.TAG_NAME, "form")
        sign_up_form = list(filter(lambda x: x.get_attribute(
            "action") == (TestConfig.base_url + "/partials/_handleSignup.php"), forms))[0]
        sign_up_form_submit_button = Client.get_element_by_innerHTML(
            sign_up_form, "Submit")
        return sign_up_form_submit_button

    @staticmethod
    def get_element_by_innerHTML(element: WebElement, innerHTML: str, by: By = By.TAG_NAME, by_value: str = "button"):
        child_elements = element.find_elements(by, by_value)
        target_element = list(
            filter(lambda x: x.get_attribute("innerHTML") == innerHTML, child_elements))[0]
        return target_element


class Server():

    mydb = mysql.connector.connect(
        host=TestConfig.db_host,
        database=TestConfig.db_name,
        user=TestConfig.db_user,
        password=TestConfig.db_password
    )

    @staticmethod
    def truncate_users_table():
        Server.mydb.cursor().execute("TRUNCATE USERS")

    @staticmethod
    def add_dummy_user(username: str):
        url = TestConfig.base_url + "/partials/_handleSignup.php"
        data = {
            "username": username,
            "firstName": "Does it",
            "lastName": "matter?",
            "email": "generic@email.com",
            "phone": "1234554321",
            "password": "apollo13",
            "cpassword": "apollo13"
        }
        requests.post(url, data)
