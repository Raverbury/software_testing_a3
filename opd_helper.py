from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector
import requests
from _test_config import TestConfig


class Client():
    """A class providing utilities to retrieve elements in the frontend of the OPD application"""

    @staticmethod
    def auto_expand_navbar(driver: WebDriver):
        """Automatically detects and expands the navbar if possible"""
        expand_button = driver.find_element(By.XPATH, "//nav//button")
        if expand_button == None:
            return
        if not expand_button.is_displayed():
            return
        if expand_button.get_attribute("aria-expanded") == "true":
            return
        expand_button.click()

    @staticmethod
    def get_signup_button(driver: WebDriver):
        """Returns the SignUp button located on the navbar"""
        Client.auto_expand_navbar(driver)
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
        buttons = driver.find_elements(By.TAG_NAME, "button")
        signup_button = list(
            filter(lambda x: x.get_attribute("innerHTML") == "SignUp", buttons))[0]
        driver.implicitly_wait(5000)
        return signup_button

    @staticmethod
    def get_login_button(driver: WebDriver):
        """Returns the Login button located on the navbar"""
        Client.auto_expand_navbar(driver)
        buttons = driver.find_elements(By.TAG_NAME, "button")
        login_button = list(
            filter(lambda x: x.get_attribute("innerHTML") == "Login", buttons))[0]
        return login_button

    @staticmethod
    def get_login_form_submit_button(driver: WebDriver):
        """Returns the Submit button within the signup modal"""
        forms = driver.find_elements(By.TAG_NAME, "form")
        login_form = list(filter(lambda x: x.get_attribute(
            "action") == (TestConfig.base_url + "/partials/_handleLogin.php"), forms))[0]
        login_form_submit_button = Client.get_element_by_innerHTML(
            login_form, "Submit")
        return login_form_submit_button

    @staticmethod
    def get_signup_form_submit_button(driver: WebDriver):
        """Returns the Submit button within the login modal"""
        forms = driver.find_elements(By.TAG_NAME, "form")
        signup_form = list(filter(lambda x: x.get_attribute(
            "action") == (TestConfig.base_url + "/partials/_handleSignup.php"), forms))[0]
        signup_form_submit_button = Client.get_element_by_innerHTML(
            signup_form, "Submit")
        return signup_form_submit_button

    @staticmethod
    def get_element_by_innerHTML(parent_element: WebElement, innerHTML: str, by: By = By.TAG_NAME, by_value: str = "button"):
        """Returns an element with matching innerHTML inside some parent element\n
        Should probably just use XPATH instead"""
        child_elements = parent_element.find_elements(by, by_value)
        target_element = list(
            filter(lambda x: x.get_attribute("innerHTML") == innerHTML, child_elements))[0]
        return target_element

    @staticmethod
    def log_in_as_dummy_user(driver: WebDriver, username: str):
        """Log in to the application with a dummy user (best paired with Server.register_dummy_user())"""
        current_url = driver.current_url
        Client.get_login_button(driver).click()
        Client.get_element(driver, By.ID, "loginusername").send_keys(username)
        Client.get_element(driver, By.ID, "loginpassword").send_keys("apollo13")
        Client.get_login_form_submit_button(driver).click()
        WebDriverWait(driver, 15).until(EC.url_changes(current_url))

    @staticmethod
    def get_cart_button(driver: WebDriver):
        """Returns the SignUp button located on the navbar"""
        Client.auto_expand_navbar(driver)
        return Client.get_element(driver, By.XPATH, "//button[@title='MyCart']")

    @staticmethod
    def get_element(driver: WebDriver, by: By, condition: str):
        """Grab an element from the DOM (will wait for it to be selectable)"""
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, condition)))
        return driver.find_element(by, condition)


class Server():
    """A class providing utilities to manipulate the backend and database of the OPD application"""

    mydb = mysql.connector.connect(
        host=TestConfig.db_host,
        database=TestConfig.db_name,
        user=TestConfig.db_user,
        password=TestConfig.db_password
    )

    @staticmethod
    def truncate_users_table():
        """Delete all records in USERS table\n
        (to fulfill the no-user-with-username-already-exists condition)"""
        Server.mydb.cursor().execute("BEGIN")
        Server.mydb.cursor().execute("TRUNCATE USERS")
        Server.mydb.cursor().execute("COMMIT")
        Server.mydb.cursor().execute("BEGIN")
        Server.mydb.cursor().execute("""INSERT INTO USERS (username, firstName, lastName, email, phone, userType, password) VALUES ('admin', 'admin', 'admin', 'admin@gmail.com', 0123456789, '1' ,'$2y$10$AAfxRFOYbl7FdN17rN3fgeiPu/xQrx6MnvRGzqjVHlGqHAM4d9T1i')""")
        Server.mydb.cursor().execute("COMMIT")
        # Server.mydb.cursor().execute("DELETE FROM USERS WHERE ID != 1")

    @staticmethod
    def truncate_viewcart_table():
        """Delete all records in VIEWCART table\n
        (to fulfill the cart-with-no-item condition)"""
        Server.mydb.cursor().execute("TRUNCATE VIEWCART")

    @staticmethod
    def register_dummy_user(username: str, driver : WebDriver):
        """Create a record in the USERS table using the provided username\n
        The rest don't really matter\n
        (to fulfill the a-user-with-username-already-exists condition)"""
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
        driver.implicitly_wait(5000)
        
