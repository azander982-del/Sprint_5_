from locators import (ACCOUNT_BUTTON, REGISTER_LINK, NAME_FIELD, EMAIL_FIELD, 
                      PASSWORD_FIELD, REGISTER_BUTTON, LOGIN_EMAIL_FIELD, BUTTON_IN)
from data import generate_random_email, generate_random_password

def test_successful_registration(driver):

    email = generate_random_email()
    password = generate_random_password()
    
    driver.find_element(*ACCOUNT_BUTTON).click()
    driver.find_element(*REGISTER_LINK).click()
    driver.find_element(*NAME_FIELD).send_keys("Тестовый пользователь")
    driver.find_element(*EMAIL_FIELD).send_keys(email)
    driver.find_element(*PASSWORD_FIELD).send_keys(password)
    driver.find_element(*REGISTER_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(email)
    driver.find_element(*PASSWORD_FIELD).send_keys(password)
    driver.find_element(*BUTTON_IN).click()
    driver.find_element(*ACCOUNT_BUTTON).click()

    assert driver.current_url == "https://stellarburgers.education-services.ru/account/profile"