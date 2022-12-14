from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from opd_helper import Client
from opd_helper import Server
from _test_config import TestConfig
from _test_config import Browser
from selenium import webdriver
import time
import pytest

driver = webdriver.Edge()
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
# if() : 

# WebDriverWait(driver, 15).until(EC.url_changes(current_url))
# Step
# test_result = driver.switchTo().alert().getText() == 'Please fill out this field.'
# test_result = driver.switch_to.alert == 'Please fill out this field.'
p = Client.get_element(driver, By.ID, "loginModal")
# message = p.get_attribute('validationMessage')
print(p.get_attribute('style'))
# validate the alert text
