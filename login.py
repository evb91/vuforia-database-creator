from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import uuid

driver = webdriver.Safari()
driver.implicitly_wait(10)
driver.get("https://developer.vuforia.com/vui/auth/login")
elem = driver.find_element_by_id("login_email")
elem.send_keys(os.environ['VUFORIA_EMAIL_ADDRESS'])
elem = driver.find_element_by_id("login_password")
elem.send_keys(os.environ['VUFORIA_PASSWORD'])
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_id("get-development-key")
elem.click()
elem = driver.find_element_by_id("license-name")
random = uuid.uuid4().hex
license_name = 'generated_license_name_' + str(random)
elem.send_keys(license_name)
elem = driver.find_element_by_id("agree-terms-checkbox")
elem.submit()
elem = driver.find_element_by_id("confirm")
elem.click()
driver.get("https://developer.vuforia.com/vui/develop/databases")
elem = driver.find_element_by_id("add-dialog-btn")
elem.click()
# elem = driver.find_element_by_id("database-name")
# elem.send_keys('foo')
# elem = driver.find_element_by_id("cloud-radio-btn")
# elem.submit()
# elem = driver.find_element_by_id("cloud-license-dropdown")
breakpoint()
# driver.close()
