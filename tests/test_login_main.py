from locators import ACCOUNT_BUTTON, PASSWORD_FIELD, BUTTON_IN, LOGIN_EMAIL_FIELD
from data import DEFAULT_PASSWORD, TEST_EMAIL

def test_login_via_account_button(driver):

    driver.find_element(*ACCOUNT_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(TEST_EMAIL)
    driver.find_element(*PASSWORD_FIELD).send_keys(DEFAULT_PASSWORD)
    driver.find_element(*BUTTON_IN).click()
    driver.find_element(*ACCOUNT_BUTTON).click()
    
    assert driver.current_url == "https://stellarburgers.education-services.ru/account/profile"