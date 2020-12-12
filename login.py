from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import uuid
import time


def create_database(vuforia_username, vuforia_password, license_name, database_name):

    driver = webdriver.Safari()
    driver.implicitly_wait(10)
    driver.get("https://developer.vuforia.com/vui/auth/login")
    elem = driver.find_element_by_id("login_email")
    elem.send_keys(vuforia_username)
    elem = driver.find_element_by_id("login_password")
    elem.send_keys(vuforia_password)
    elem.send_keys(Keys.RETURN)
    elem = driver.find_element_by_id("get-development-key")
    elem.click()
    elem = driver.find_element_by_id("license-name")
    elem.send_keys(license_name)
    elem = driver.find_element_by_id("agree-terms-checkbox")
    elem.submit()
    elem = driver.find_element_by_id("confirm")
    elem.click()
    driver.get("https://developer.vuforia.com/vui/develop/databases")
    elem = driver.find_element_by_id("add-dialog-btn")
    time.sleep(5)
    elem.click()
    elem = driver.find_element_by_id("database-name")
    elem.send_keys(database_name)
    elem = driver.find_element_by_id("cloud-radio-btn")
    elem.click()
    license_name_dashes = license_name.replace("_", "-")
    license_dropdown_id = "cloud-license-" + license_name_dashes
    elem = driver.find_element_by_id(license_dropdown_id)
    time.sleep(5)
    elem.click()
    elem = driver.find_element_by_id("create-btn")
    elem.click()
    database_name_xpath = "//span[text()='" + database_name + "']"
    elem = driver.find_element_by_xpath(database_name_xpath)
    elem.click()
    time.sleep(5)
    elem = driver.find_element_by_link_text("Database Access Keys")
    elem.click()
    elem = driver.find_element_by_class_name("client-access-key")
    client_access_key = elem.text
    elem = driver.find_element_by_class_name("client-secret-key")
    client_secret_key = elem.text
    elem = driver.find_element_by_class_name("server-access-key")
    server_access_key = elem.text
    elem = driver.find_element_by_class_name("server-secret-key")
    server_secret_key = elem.text
    driver.close()


random = uuid.uuid4().hex
vuforia_username = os.environ["VUFORIA_EMAIL_ADDRESS"]
vuforia_password = os.environ["VUFORIA_PASSWORD"]
license_name = "generated_license_name_" + str(random)
database_name = "database_name_" + str(random)

create_database(
    vuforia_username=vuforia_username,
    vuforia_password=vuforia_password,
    license_name=license_name,
    database_name=database_name,
)
