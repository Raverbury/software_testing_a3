from selenium import webdriver


class Browser():
    FIREFOX = "firefox"
    CHROME = "chrome"
    EDGE = "edge"


class TestConfig():

    browser = Browser.FIREFOX
    """The browser used to carry out tests\n
    Supported values: ["firefox", "chrome", "edge"]"""

    @staticmethod
    def get_browser():
        if TestConfig.browser == "firefox":
            return webdriver.Firefox()
        elif TestConfig.browser == "chrome":
            return webdriver.Chrome()
        elif TestConfig.browser == "edge":
            return webdriver.Edge()
        else:
            return None

    base_url = "http://localhost/OnlinePizzaDelivery"
    """The base URL of the OnlinePizzaDelivery website"""

    db_host = "localhost"
    """The host of the database used in the application"""
    db_name = "OPD"
    """The database name of the database used in the application"""
    db_user = "root"
    """The username of the database used in the application"""
    db_password = ""
    """The password of the database used in the application"""
