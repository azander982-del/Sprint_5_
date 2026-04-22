from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import ACCOUNT_BUTTON, PASSWORD_FIELD, BUTTON_IN, LOGIN_EMAIL_FIELD,LOGO, BUTTON_IN_MAIN
from data import generate_random_email, DEFAULT_PASSWORD, TEST_EMAIL
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.education-services.ru/")
driver.find_element(*BUTTON_IN_MAIN).click()
driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(TEST_EMAIL)
driver.find_element(*PASSWORD_FIELD).send_keys(DEFAULT_PASSWORD)
driver.find_element(*BUTTON_IN).click()
driver.find_element(*ACCOUNT_BUTTON).click()
time.sleep(2)
driver.find_element(*LOGO).click()
time.sleep(2)
assert driver.current_url == "https://stellarburgers.education-services.ru/"


driver.quit()