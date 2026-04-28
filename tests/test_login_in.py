from locators import ACCOUNT_BUTTON, REGISTER_LINK, PASSWORD_FIELD, BUTTON_IN, LOGIN_EMAIL_FIELD, BUTTON_IN_MAIN, REGISTER_BUTTON_REG
from data import DEFAULT_PASSWORD, TEST_EMAIL

def test_login_via_registration_button(driver):
    
    driver.find_element(*BUTTON_IN_MAIN).click()
    driver.find_element(*REGISTER_LINK).click()
    driver.find_element(*REGISTER_BUTTON_REG).click()
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(TEST_EMAIL)
    driver.find_element(*PASSWORD_FIELD).send_keys(DEFAULT_PASSWORD)
    driver.find_element(*BUTTON_IN).click()
    driver.find_element(*ACCOUNT_BUTTON).click()

    assert driver.current_url == "https://stellarburgers.education-services.ru/account/profile"