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
# p = Client.get_element(driver, By.ID, "loginModal")

# button = driver.find_element(By.CLASS_NAME, "close")
# button.click()
# driver.implicitly_wait(5000)
# try: 
#     modal  = driver.find_element(By.CLASS_NAME, "modal.fade")
#     print
# except:
    

# message = p.get_attribute('validationMessage')
# print(p.get_attribute('style'))
# validate the alert text

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
print(message)