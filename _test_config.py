from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Browser():
    FIREFOX = "firefox"
    CHROME = "chrome"
    EDGE = "edge"


class TestConfig():
    """A class to store test configurations"""

    browser = Browser.FIREFOX
    """<<EDITABLE>> The browser used to carry out tests\n
    Supported values: ["firefox", "chrome", "edge"] (or just use the Browser enums)"""

    base_url = "http://localhost/OnlinePizzaDelivery"
    """<<EDITABLE>> The base URL of the OnlinePizzaDelivery website, without trailing slash"""

    db_host = "localhost"
    """<<EDITABLE>> The host of the database used in the application"""
    db_name = "OPD"
    """<<EDITABLE>> The database name of the database used in the application"""
    db_user = "root"
    """<<EDITABLE>> The username of the database used in the application"""
    db_password = ""
    """<<EDITABLE>> The password of the database used in the application"""

    @staticmethod
    def get_default_browser():
        return TestConfig.get_browser(TestConfig.browser, False)

    @staticmethod
    def get_browser(browser: str, small_screen_size: bool):
        driver = None
        if browser == "firefox":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "edge":
            driver = webdriver.Edge()
        else:
            return None
        if small_screen_size:
            driver.set_window_size(360, 640)
        return driver
