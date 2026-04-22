from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import ACCOUNT_BUTTON, PASSWORD_FIELD, BUTTON_IN, LOGIN_EMAIL_FIELD, BUTTON_IN_MAIN, REGEN_BUTTTON,  REGISTER_BUTTON_REG
from data import  DEFAULT_PASSWORD, TEST_EMAIL
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.education-services.ru/")

driver.find_element(*BUTTON_IN_MAIN).click()
driver.find_element(*REGEN_BUTTTON).click()
driver.find_element(*REGISTER_BUTTON_REG).click()
driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(TEST_EMAIL)
driver.find_element(*PASSWORD_FIELD).send_keys(DEFAULT_PASSWORD)
driver.find_element(*BUTTON_IN).click()
driver.find_element(*ACCOUNT_BUTTON).click()
time.sleep(2)
assert driver.current_url == "https://stellarburgers.education-services.ru/account/profile"


driver.quit()