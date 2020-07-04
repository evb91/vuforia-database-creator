from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
driver.get("https://developer.vuforia.com/vui/auth/login")
elem = driver.find_element_by_id("login_email")
elem.send_keys("pycon")
elem = driver.find_element_by_id("login_password")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
# driver.close()
