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
    "browser,small_screen_size",
    [
        (Browser.EDGE, False),
        (Browser.EDGE, True)
    ],
)
class TestSignUp():

    @staticmethod
    def test_OPD_001_001(browser: str, small_screen_size: str):
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            Server.truncate_users_table()
            driver.get(TestConfig.base_url)
            current_url = driver.current_url
            # steps

            signup = Client.get_signup_button(driver)
            
            signup.click()
            
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "username")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "firstName")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "lastName")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "email")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "phone")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cpassword")))
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
    def test_OPD_001_002(browser: str, small_screen_size: str):
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            Server.truncate_users_table()
            Server.register_dummy_user("testuser_02", driver)
            driver.get(TestConfig.base_url)
            current_url = driver.current_url
            # steps
            Client.get_signup_button(driver).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "username")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "firstName")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "lastName")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "email")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "phone")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cpassword")))
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
    def test_OPD_001_003(browser: str, small_screen_size: str):
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            Server.truncate_users_table()
            driver.get(TestConfig.base_url)
            current_url = driver.current_url
            # steps
            Client.get_signup_button(driver).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "username")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "firstName")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "lastName")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "email")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "phone")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cpassword")))
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
    def test_OPD_001_004(browser: str, small_screen_size: str):
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            Server.truncate_users_table()
            Server.register_dummy_user("testuser_02", driver)
            driver.get(TestConfig.base_url)
            current_url = driver.current_url
            # steps
            Client.get_signup_button(driver).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "username")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "firstName")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "lastName")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "email")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "phone")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cpassword")))
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
    def test_OPD_001_005(browser: str, small_screen_size: str):
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            driver.get(TestConfig.base_url)
            # steps
            Client.get_signup_button(driver).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "username")))

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
    def test_OPD_001_006(browser: str, small_screen_size: str):
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            driver.get(TestConfig.base_url)
            # steps
            Client.get_signup_button(driver).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "username")))
 
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
    def test_OPD_001_007(browser: str, small_screen_size: str):
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            driver.get(TestConfig.base_url)
            # steps
            Client.get_signup_button(driver).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "username")))
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
    def test_OPD_001_008(browser: str, small_screen_size: str):
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            driver.get(TestConfig.base_url)
            # steps
            Client.get_signup_button(driver).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "username")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "firstName")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "lastName")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "email")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "phone")))
            # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
            # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cpassword")))
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
    def test_OPD_001_009(browser: str, small_screen_size: str):
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            driver.get(TestConfig.base_url)
            # steps
            Client.get_signup_button(driver).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "username")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "firstName")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "lastName")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "email")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "phone")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cpassword")))
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
    def test_OPD_001_010(browser: str, small_screen_size: str):
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            Server.truncate_users_table()
            driver.get(TestConfig.base_url)
            current_url = driver.current_url
            # steps
            Client.get_signup_button(driver).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "username")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "firstName")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "lastName")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "email")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "phone")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cpassword")))
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
    def test_OPD_001_011(browser: str, small_screen_size: str):
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            Server.truncate_users_table()
            driver.get(TestConfig.base_url)
            current_url = driver.current_url
            # steps
            Client.get_signup_button(driver).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "username")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "firstName")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "lastName")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "email")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "phone")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cpassword")))
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
    "browser,small_screen_size",
    [
        (Browser.EDGE, False),
        (Browser.EDGE, True)
    ],
)
class TestOrder():

    @staticmethod
    def test_OPD_004_001(browser: str, small_screen_size: str):
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            Server.truncate_users_table()
            Server.truncate_viewcart_table()
            Server.register_dummy_user("testuser_09", driver)
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
    def test_OPD_004_002(browser: str, small_screen_size: str):
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            Server.truncate_users_table()
            Server.truncate_viewcart_table()
            Server.register_dummy_user("testuser_09", driver)
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
    def test_OPD_004_003(browser: str, small_screen_size: str):
        driver = TestConfig.get_browser(browser, small_screen_size)
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
    "browser,small_screen_size",
    [
        (Browser.EDGE, False),
        (Browser.EDGE, True)
    ],
)
class TestLogin():
    @staticmethod
    def test_OPD_002_001(browser: str, small_screen_size: str): # Login successfully
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            Server.truncate_users_table()
            Server.truncate_viewcart_table()
            Server.register_dummy_user("testuser_09", driver)
            driver.get(TestConfig.base_url)
            Client.log_in_as_dummy_user(driver, "testuser_09")
            # Step
            current_url = driver.current_url
            test_result = 'You are logged in' in driver.page_source
            # test_result = current_url == TestConfig.base_url+'/index.php?loginsuccess=true'

        except:
            test_result = False
        finally:
            driver.close()
        assert test_result



    @staticmethod
    def test_OPD_002_002(browser: str, small_screen_size: str): # Login successfully
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            Server.truncate_users_table()
            Server.truncate_viewcart_table()
            Server.register_dummy_user("testuser_09", driver)
            driver.get(TestConfig.base_url)
            # Client.log_in_as_dummy_user(driver, "testuser_09")
            current_url = driver.current_url
            Client.get_login_button(driver).click()
            Client.get_element(driver, By.ID, "loginusername").send_keys('testuser242')
            Client.get_element(driver, By.ID, "loginpassword").send_keys("testuser_02")
            Client.get_login_form_submit_button(driver).click()
            WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            # Step
            test_result = 'Invalid Credentials' in driver.page_source

        except:
            test_result = False
        finally:
            driver.close()
        assert test_result


    @staticmethod
    def test_OPD_002_003(browser: str, small_screen_size: str): # Login successfully
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            Server.truncate_users_table()
            Server.truncate_viewcart_table()
            Server.register_dummy_user("testuser_09", driver)
            driver.get(TestConfig.base_url)
            # Client.log_in_as_dummy_user(driver, "testuser_09")
            current_url = driver.current_url
            Client.get_login_button(driver).click()
            Client.get_element(driver, By.ID, "loginusername").send_keys('testuser242')
            Client.get_element(driver, By.ID, "loginpassword").send_keys("testuser_02")
            Client.get_login_form_submit_button(driver).click()
            WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            # Step
            test_result = 'Invalid Credentials' in driver.page_source

        except:
            test_result = False
        finally:
            driver.close()
        assert test_result


    @staticmethod
    def test_OPD_002_004(browser: str, small_screen_size: str): # Login successfully
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            Server.truncate_users_table()
            Server.truncate_viewcart_table()
            Server.register_dummy_user("testuser_09", driver)
            driver.get(TestConfig.base_url)
            # Client.log_in_as_dummy_user(driver, "testuser_09")
            current_url = driver.current_url
            Client.get_login_button(driver).click()
            Client.get_element(driver, By.ID, "loginusername").send_keys('12')
            Client.get_element(driver, By.ID, "loginpassword").send_keys("12")
            Client.get_login_form_submit_button(driver).click()
            WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            # Step
            test_result = 'Invalid Credentials' in driver.page_source

        except:
            test_result = False
        finally:
            driver.close()
        assert test_result

    @staticmethod
    def test_OPD_002_005(browser: str, small_screen_size: str): # Login successfully
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            Server.truncate_users_table()
            Server.truncate_viewcart_table()
            Server.register_dummy_user("testuser_09", driver)
            driver.get(TestConfig.base_url)
            # Client.log_in_as_dummy_user(driver, "testuser_09")
            current_url = driver.current_url
            Client.get_login_button(driver).click()
            Client.get_element(driver, By.ID, "loginusername").send_keys('12')
            Client.get_element(driver, By.ID, "loginpassword").send_keys("12")
            Client.get_login_form_submit_button(driver).click()
            WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            # Step
            test_result = 'Invalid Credentials' in driver.page_source

        except:
            test_result = False
        finally:
            driver.close()
        assert test_result

    @staticmethod
    def test_OPD_002_006(browser: str, small_screen_size: str): # Login successfully
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            Server.truncate_users_table()
            Server.truncate_viewcart_table()
            Server.register_dummy_user("testuser_09", driver)
            driver.get(TestConfig.base_url)
            # Client.log_in_as_dummy_user(driver, "testuser_09")
            current_url = driver.current_url
            Client.get_login_button(driver).click()
            Client.get_element(driver, By.ID, "loginusername").send_keys('12')
            Client.get_element(driver, By.ID, "loginpassword").send_keys("")
            Client.get_login_form_submit_button(driver).click()

            password = Client.get_element(driver, By.ID, "loginpassword")
            message = password.get_attribute('validationMessage')
            test_result = message == 'Please fill out this field.'
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result

    @staticmethod
    def test_OPD_002_007(browser: str, small_screen_size: str): # Login successfully
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            Server.truncate_users_table()
            Server.truncate_viewcart_table()
            Server.register_dummy_user("testuser_09", driver)
            driver.get(TestConfig.base_url)
            # Client.log_in_as_dummy_user(driver, "testuser_09")
            current_url = driver.current_url
            Client.get_login_button(driver).click()
            Client.get_element(driver, By.ID, "loginusername").send_keys('')
            Client.get_element(driver, By.ID, "loginpassword").send_keys("testuser242")
            Client.get_login_form_submit_button(driver).click()

            username = Client.get_element(driver, By.ID, "loginusername")
            message = username.get_attribute('validationMessage')
            test_result = message == 'Please fill out this field.'
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result

    @staticmethod
    def test_OPD_002_008(browser: str, small_screen_size: str): # Login successfully
        driver = TestConfig.get_browser(browser, small_screen_size)
        try :
            # preparations
            Server.truncate_users_table()
            Server.truncate_viewcart_table()
            Server.register_dummy_user("testuser_09", driver)

            driver.get(TestConfig.base_url)
            # # Client.log_in_as_dummy_user(driver, "testuser_09")
            # current_url = driver.current_url
            # Client.get_login_button(driver).click()
            
            Client.get_login_button(driver).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "close")))
            button = driver.find_element(By.CLASS_NAME, "close")
            button.click()
            modal  = driver.find_element(By.CLASS_NAME, "modal.fade")
            test_result = True
            # Client.get_element(driver, By.ID, "loginusername").send_keys('')
            # Client.get_element(driver, By.ID, "loginpassword").send_keys("testuser242")
            # Client.get_login_form_submit_button(driver).click()

            # username = Client.get_element(driver, By.ID, "loginusername")
            # message = username.get_attribute('validationMessage')
            # test_result = message == 'Please fill out this field.'
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result


    @staticmethod
    def test_OPD_002_009(browser: str, small_screen_size: str): # Login successfully
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            Server.truncate_users_table()
            Server.truncate_viewcart_table()
            Server.register_dummy_user("testuser_09", driver)
            driver.get(TestConfig.base_url)
            # Client.log_in_as_dummy_user(driver, "testuser_09")
            current_url = driver.current_url
            Client.get_login_button(driver).click()
            Client.get_element(driver, By.ID, "loginusername").send_keys('12111111111111111111')
            Client.get_element(driver, By.ID, "loginpassword").send_keys("12111111111111111111")
            Client.get_login_form_submit_button(driver).click()
            WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            # Step
            test_result = 'Invalid Credentials' in driver.page_source

        except:
            test_result = False
        finally:
            driver.close()
        assert test_result


    @staticmethod
    def test_OPD_002_010(browser: str, small_screen_size: str): # Login successfully
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            Server.truncate_users_table()
            Server.truncate_viewcart_table()
            Server.register_dummy_user("testuser_09", driver)
            driver.get(TestConfig.base_url)
            # Client.log_in_as_dummy_user(driver, "testuser_09")
            current_url = driver.current_url
            Client.get_login_button(driver).click()
            Client.get_element(driver, By.ID, "loginusername").send_keys('12111111111111111111')
            Client.get_element(driver, By.ID, "loginpassword").send_keys("12111111111111111111")
            Client.get_login_form_submit_button(driver).click()
            WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            # Step
            test_result = 'Invalid Credentials' in driver.page_source

        except:
            test_result = False
        finally:
            driver.close()
        assert test_result



@pytest.mark.parametrize(
    "browser,small_screen_size",
    [
        (Browser.EDGE, False),
        (Browser.EDGE, True)
    ],
)
class TestOrderAdmin():
    @staticmethod
    def test_OPD_005_001(browser: str, small_screen_size: str):
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            # Server.truncate_users_table()
            # Server.truncate_viewcart_table()
            # Server.register_dummy_user("testuser_09", driver)
            Server.prepare_data_for_admin()
            driver.implicitly_wait(5000)
            driver.get(TestConfig.base_url+'/admin/login.php')
            Client.log_in_as_admin(driver, "admin")
            # driver.get(TestConfig.base_url + "/viewPizzaList.php?catid=1")
            current_url = driver.current_url
            driver.get('http://localhost/OnlinePizzaDelivery/admin/index.php?page=orderManage')
            test_result =Client.update_order(driver, 2)
         
            # test_result = True

       
            # #steps
            # margherita_add_to_cart_button = driver.find_element(
            #     By.XPATH, "//div[./h5[contains(text(),'Margherita...')]]//button[@name='addToCart']")
            # margherita_add_to_cart_button.click()
            # time.sleep(2)
            # current_url = driver.current_url
            # Client.get_cart_button(driver).click()
            # WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            # # expected result
            # test_result = True
            # test_result = (
            #     TestConfig.base_url + "/viewCart.php") == driver.current_url and "Margherita" in driver.page_source
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result


    @staticmethod
    def test_OPD_005_002(browser: str, small_screen_size: str):
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            # Server.truncate_users_table()
            # Server.truncate_viewcart_table()
            # Server.register_dummy_user("testuser_09", driver)
            driver.get(TestConfig.base_url+'/admin/login.php')
            Client.log_in_as_admin(driver, "admin")
            # driver.get(TestConfig.base_url + "/viewPizzaList.php?catid=1")
            current_url = driver.current_url
            driver.get('http://localhost/OnlinePizzaDelivery/admin/index.php?page=orderManage')
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'view')))
            driver.implicitly_wait(2000)
            driver.find_elements(By.CLASS_NAME, "view")[0].click()
            status_btn = Client.get_element(driver, By.ID, "status")
            status_btn.clear()
            status_btn.send_keys('60')
            Client.get_element(driver, By.CLASS_NAME, "btn.btn-success.mb-2").click()
            status = Client.get_element(driver, By.ID, "status")
            message = status.get_attribute('validationMessage')
            test_result = message == 'Value must be less than or equal to 6.'
            # Client.get_login_form_submit_button(driver).click()
            # WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            # alert = driver.switch_to.alert
            # alert.accept()
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result


    @staticmethod
    def test_OPD_005_003(browser: str, small_screen_size: str):
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            # Server.truncate_users_table()
            # Server.truncate_viewcart_table()
            # Server.register_dummy_user("testuser_09", driver)
            driver.get(TestConfig.base_url+'/admin/login.php')
            Client.log_in_as_admin(driver, "admin")
            # driver.get(TestConfig.base_url + "/viewPizzaList.php?catid=1")
            current_url = driver.current_url
            driver.get('http://localhost/OnlinePizzaDelivery/admin/index.php?page=orderManage')
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'view')))
            driver.implicitly_wait(2000)
            driver.find_elements(By.CLASS_NAME, "view")[0].click()
            status_btn = Client.get_element(driver, By.ID, "status")
            status_btn.clear()
            status_btn.send_keys('1')
            Client.get_element(driver, By.CLASS_NAME, "btn.btn-success.mb-2").click()
            # Client.get_login_form_submit_button(driver).click()
            # WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            alert = driver.switch_to.alert
            alert.accept()
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'view')))
            driver.implicitly_wait(2000)
            driver.find_elements(By.CLASS_NAME, "view")[0].click()
            name = Client.get_element(driver, By.ID, "name")
            name.clear()
            name.send_keys('huy cao')

            phone = Client.get_element(driver, By.ID, "phone")
            phone.clear()
            phone.send_keys('00000000000000000')
            time = Client.get_element(driver, By.ID, "time")
            time.clear()
            time.send_keys('120')
            driver.find_elements(By.CLASS_NAME, "btn.btn-success")[1].click()
            message = phone.get_attribute('validationMessage')
            test_result = message == 'Please match the requested format.'
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result


    @staticmethod
    def test_OPD_005_004(browser: str, small_screen_size: str):
        driver = TestConfig.get_browser(browser, small_screen_size)
        try:
            # preparations
            driver.get(TestConfig.base_url+'/admin/login.php')
            Client.log_in_as_admin(driver, "admin")
            # driver.get(TestConfig.base_url + "/viewPizzaList.php?catid=1")
            current_url = driver.current_url
            driver.get('http://localhost/OnlinePizzaDelivery/admin/index.php?page=orderManage')
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'view')))
            driver.implicitly_wait(2000)
            driver.find_elements(By.CLASS_NAME, "view")[0].click()
            status_btn = Client.get_element(driver, By.ID, "status")
            status_btn.clear()
            status_btn.send_keys('1')
            Client.get_element(driver, By.CLASS_NAME, "btn.btn-success.mb-2").click()
            # Client.get_login_form_submit_button(driver).click()
            # WebDriverWait(driver, 15).until(EC.url_changes(current_url))
            alert = driver.switch_to.alert
            alert.accept()
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'view')))
            driver.implicitly_wait(2000)
            driver.find_elements(By.CLASS_NAME, "view")[0].click()
            name = Client.get_element(driver, By.ID, "name")
            name.clear()
            name.send_keys('huy cao')

            phone = Client.get_element(driver, By.ID, "phone")
            phone.clear()
            phone.send_keys('0794733033')
            time = Client.get_element(driver, By.ID, "time")
            time.clear()
            time.send_keys('200')
            driver.find_elements(By.CLASS_NAME, "btn.btn-success")[1].click()
            message = time.get_attribute('validationMessage')
            test_result = message == 'Value must be less than or equal to 120.'
        except:
            test_result = False
        finally:
            driver.close()
        assert test_result
