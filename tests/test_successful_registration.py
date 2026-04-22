from selenium import webdriver
from locators import ACCOUNT_BUTTON, REGISTER_LINK, NAME_FIELD, EMAIL_FIELD, PASSWORD_FIELD, REGISTER_BUTTON
from data import generate_random_email, generate_random_password
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.education-services.ru/")

driver.find_element(*ACCOUNT_BUTTON).click()
time.sleep(2)

driver.find_element(*REGISTER_LINK).click()

driver.find_element(*NAME_FIELD).send_keys("Тестовый пользователь")
driver.find_element(*EMAIL_FIELD).send_keys(generate_random_email())
driver.find_element(*PASSWORD_FIELD).send_keys(generate_random_password())

driver.find_element(*REGISTER_BUTTON).click()
time.sleep(2)

assert driver.current_url == "https://stellarburgers.education-services.ru/login"


driver.quit()