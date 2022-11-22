from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from opd_helper import Client
from opd_helper import Server
from _test_config import TestConfig
from _test_config import Browser
import time
import pytest


@pytest.mark.parametrize(
    "browser",
    [
        Browser.FIREFOX,
        Browser.EDGE
    ],
)
class TestSignUp():

    @staticmethod
    def test_OPD_001_001(browser: str):
        driver = TestConfig.get_browser(browser)
        try:
            # preparations
            Server.truncate_users_table()
            driver.get(TestConfig.base_url)
            current_url = driver.current_url
            # steps
            Client.get_signup_button(driver).click()
            driver.find_element(By.ID, "username").send_keys("testuser_02")
            driver.find_element(By.ID, "firstName").send_keys("Shadow")
            driver.find_element(By.ID, "lastName").send_keys("Raccoon")
            driver.find_element(By.ID, "email").send_keys(
                "testemail72@gmail.com")
            driver.find_element(By.ID, "phone").send_keys("1234567891")
            driver.find_element(By.ID, "password").send_keys("hypothermia")
            driver.find_element(By.ID, "cpassword").send_keys("hypothermia")
            Client.get_signup_form_submit_button(driver).click()
            WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            # expected result
            test_result = "You can now login" in driver.page_source
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result

    @staticmethod
    def test_OPD_001_002(browser: str):
        driver = TestConfig.get_browser(browser)
        try:
            # preparations
            Server.truncate_users_table()
            Server.register_dummy_user("testuser_02")
            driver.get(TestConfig.base_url)
            current_url = driver.current_url
            # steps
            Client.get_signup_button(driver).click()
            driver.find_element(By.ID, "username").send_keys("testuser_02")
            driver.find_element(By.ID, "firstName").send_keys("Shadow")
            driver.find_element(By.ID, "lastName").send_keys("Raccoon")
            driver.find_element(By.ID, "email").send_keys(
                "testemail72@gmail.com")
            driver.find_element(By.ID, "phone").send_keys("1234567891")
            driver.find_element(By.ID, "password").send_keys("hypothermia")
            driver.find_element(By.ID, "cpassword").send_keys("hypothermia")
            Client.get_signup_form_submit_button(driver).click()
            WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            # expected result
            test_result = "Username Already Exists" in driver.page_source
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result

    @staticmethod
    def test_OPD_001_003(browser: str):
        driver = TestConfig.get_browser(browser)
        try:
            # preparations
            Server.truncate_users_table()
            driver.get(TestConfig.base_url)
            current_url = driver.current_url
            # steps
            Client.get_signup_button(driver).click()
            driver.find_element(By.ID, "username").send_keys("testuser_02")
            driver.find_element(By.ID, "firstName").send_keys("Shadow")
            driver.find_element(By.ID, "lastName").send_keys("Raccoon")
            driver.find_element(By.ID, "email").send_keys(
                "testemail72@gmail.com")
            driver.find_element(By.ID, "phone").send_keys("1234567891")
            driver.find_element(By.ID, "password").send_keys("hypothermia")
            driver.find_element(By.ID, "cpassword").send_keys("singularity")
            Client.get_signup_form_submit_button(driver).click()
            WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            # expected result
            test_result = "Passwords do not match" in driver.page_source
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result

    @staticmethod
    def test_OPD_001_004(browser: str):
        driver = TestConfig.get_browser(browser)
        try:
            # preparations
            Server.truncate_users_table()
            Server.register_dummy_user("testuser_02")
            driver.get(TestConfig.base_url)
            current_url = driver.current_url
            # steps
            Client.get_signup_button(driver).click()
            driver.find_element(By.ID, "username").send_keys("testuser_02")
            driver.find_element(By.ID, "firstName").send_keys("Shadow")
            driver.find_element(By.ID, "lastName").send_keys("Raccoon")
            driver.find_element(By.ID, "email").send_keys(
                "testemail72@gmail.com")
            driver.find_element(By.ID, "phone").send_keys("1234567891")
            driver.find_element(By.ID, "password").send_keys("hypothermia")
            driver.find_element(By.ID, "cpassword").send_keys("singularity")
            Client.get_signup_form_submit_button(driver).click()
            WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            # expected result
            test_result = "Username Already Exists" in driver.page_source
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result

    @staticmethod
    def test_OPD_001_005(browser: str):
        driver = TestConfig.get_browser(browser)
        try:
            # preparations
            driver.get(TestConfig.base_url)
            # steps
            Client.get_signup_button(driver).click()
            driver.find_element(By.ID, "username").send_keys("gg")
            Client.get_signup_form_submit_button(driver).click()
            # expected result
            test_result = all(map(lambda x: x in driver.find_element(By.ID, "username").get_attribute(
                "validationMessage"), ["3 characters", "(you are currently using 2 character"]))
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result

    @staticmethod
    def test_OPD_001_006(browser: str):
        driver = TestConfig.get_browser(browser)
        try:
            # preparations
            driver.get(TestConfig.base_url)
            # steps
            Client.get_signup_button(driver).click()
            username_field = driver.find_element(By.ID, "username")
            username_field.send_keys("1")
            Client.get_signup_form_submit_button(driver).click()
            er_1 = all(map(lambda x: x in driver.find_element(By.ID, "username").get_attribute(
                "validationMessage"), ["3 characters", "(you are currently using 1 character"]))
            username_field.clear()
            username_field.send_keys("12")
            Client.get_signup_form_submit_button(driver).click()
            er_2 = all(map(lambda x: x in driver.find_element(By.ID, "username").get_attribute(
                "validationMessage"), ["3 characters", "(you are currently using 2 character"]))
            # expected result
            test_result = er_1 and er_2
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result

    @staticmethod
    def test_OPD_001_007(browser: str):
        driver = TestConfig.get_browser(browser)
        try:
            # preparations
            driver.get(TestConfig.base_url)
            # steps
            Client.get_signup_button(driver).click()
            username_field = driver.find_element(By.ID, "username")
            username_field.send_keys("poincare1234")
            # expected result
            test_result = username_field.get_attribute(
                "value") == "poincare123"
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result

    @staticmethod
    def test_OPD_001_008(browser: str):
        driver = TestConfig.get_browser(browser)
        try:
            # preparations
            driver.get(TestConfig.base_url)
            # steps
            Client.get_signup_button(driver).click()
            driver.find_element(By.ID, "username").send_keys("dual_randomness")
            driver.find_element(By.ID, "firstName").send_keys("Upper")
            driver.find_element(By.ID, "lastName").send_keys("Dark")
            driver.find_element(By.ID, "email").send_keys(
                "testemail72@gmail.com")
            driver.find_element(By.ID, "phone").send_keys("360mlg_pro")
            # expected result
            test_result = driver.find_element(By.ID, "phone").get_attribute(
                "validationMessage") == "Please match the requested format."
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result

    @staticmethod
    def test_OPD_001_009(browser: str):
        driver = TestConfig.get_browser(browser)
        try:
            # preparations
            driver.get(TestConfig.base_url)
            # steps
            Client.get_signup_button(driver).click()
            driver.find_element(By.ID, "username").send_keys("fixed_point")
            driver.find_element(By.ID, "firstName").send_keys("Lower")
            driver.find_element(By.ID, "lastName").send_keys("Dark")
            driver.find_element(By.ID, "email").send_keys(
                "testemail72@gmail.com")
            driver.find_element(By.ID, "phone").send_keys("123456789")
            driver.find_element(By.ID, "password").send_keys("hypothermia")
            driver.find_element(By.ID, "cpassword").send_keys("hypothermia")
            # expected result
            test_result = driver.find_element(By.ID, "phone").get_attribute(
                "validationMessage") == "Please match the requested format."
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result

    @staticmethod
    def test_OPD_001_010(browser: str):
        driver = TestConfig.get_browser(browser)
        try:
            # preparations
            Server.truncate_users_table()
            driver.get(TestConfig.base_url)
            current_url = driver.current_url
            # steps
            Client.get_signup_button(driver).click()
            driver.find_element(By.ID, "username").send_keys("tes")
            driver.find_element(By.ID, "firstName").send_keys("Shadow")
            driver.find_element(By.ID, "lastName").send_keys("Raccoon")
            driver.find_element(By.ID, "email").send_keys(
                "testemail72@gmail.com")
            driver.find_element(By.ID, "phone").send_keys("1234567891")
            driver.find_element(By.ID, "password").send_keys("hypothermia")
            driver.find_element(By.ID, "cpassword").send_keys("hypothermia")
            Client.get_signup_form_submit_button(driver).click()
            WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            # expected result
            test_result = "You can now login" in driver.page_source
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result

    @staticmethod
    def test_OPD_001_011(browser: str):
        driver = TestConfig.get_browser(browser)
        try:
            # preparations
            Server.truncate_users_table()
            driver.get(TestConfig.base_url)
            current_url = driver.current_url
            # steps
            Client.get_signup_button(driver).click()
            driver.find_element(By.ID, "username").send_keys("testuse")
            driver.find_element(By.ID, "firstName").send_keys("Shadow")
            driver.find_element(By.ID, "lastName").send_keys("Raccoon")
            driver.find_element(By.ID, "email").send_keys(
                "testemail72@gmail.com")
            driver.find_element(By.ID, "phone").send_keys("1234567891")
            driver.find_element(By.ID, "password").send_keys("hypothermia")
            driver.find_element(By.ID, "cpassword").send_keys("hypothermia")
            Client.get_signup_form_submit_button(driver).click()
            WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            # expected result
            test_result = "You can now login" in driver.page_source
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result


@pytest.mark.parametrize(
    "browser",
    [
        Browser.FIREFOX,
        Browser.EDGE
    ],
)
class TestOrder():

    @staticmethod
    def test_OPD_004_001(browser: str):
        driver = TestConfig.get_browser(browser)
        try:
            # preparations
            Server.truncate_users_table()
            Server.truncate_viewcart_table()
            Server.register_dummy_user("testuser_09")
            driver.get(TestConfig.base_url)
            Client.log_in_as_dummy_user(driver, "testuser_09")
            driver.get(TestConfig.base_url + "/viewPizzaList.php?catid=1")
            current_url = driver.current_url
            # steps
            margherita_add_to_cart_button = driver.find_element(
                By.XPATH, "//div[./h5[contains(text(),'Margherita...')]]//button[@name='addToCart']")
            margherita_add_to_cart_button.click()
            time.sleep(2)
            current_url = driver.current_url
            Client.get_cart_button(driver).click()
            WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            # expected result
            test_result = (
                TestConfig.base_url + "/viewCart.php") == driver.current_url and "Margherita" in driver.page_source
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result

    @staticmethod
    def test_OPD_004_002(browser: str):
        driver = TestConfig.get_browser(browser)
        try:
            # preparations
            Server.truncate_users_table()
            Server.truncate_viewcart_table()
            Server.register_dummy_user("testuser_09")
            driver.get(TestConfig.base_url)
            Client.log_in_as_dummy_user(driver, "testuser_09")
            driver.get(TestConfig.base_url + "/viewPizzaList.php?catid=1")
            current_url = driver.current_url
            margherita_add_to_cart_button = driver.find_element(
                By.XPATH, "//div[./h5[contains(text(),'Margherita...')]]//button[@name='addToCart']")
            margherita_add_to_cart_button.click()
            current_url = driver.current_url
            Client.get_cart_button(driver).click()
            WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            # steps
            driver.find_element(
                By.XPATH, "//button[@name='removeAllItem']").click()
            WebDriverWait(driver, 15).until(EC.alert_is_present())
            driver.switch_to.alert.accept()
            time.sleep(2)
            # expected result
            test_result = (
                TestConfig.base_url + "/viewCart.php") == driver.current_url and "Add something to make me happy :)" in driver.page_source
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result

    @staticmethod
    def test_OPD_004_003(browser: str):
        driver = TestConfig.get_browser(browser)
        try:
            # preparations
            driver.get(TestConfig.base_url)
            current_url = driver.current_url
            # steps
            Client.get_cart_button(driver).click()
            WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            # expected result
            test_result = (
                TestConfig.base_url + "/viewCart.php") == driver.current_url and "Before checkout you need to" in driver.page_source
        except:
            test_result = False
        finally:
            driver.close()
            pass
        assert test_result


@pytest.mark.parametrize(
    "browser",
    [
        Browser.FIREFOX,
        Browser.EDGE
    ],
)
class TestIsolate():
    pass
