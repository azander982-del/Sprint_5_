from selenium.webdriver.common.by import By
from locators import ACCOUNT_BUTTON, PASSWORD_FIELD, BUTTON_IN, LOGIN_EMAIL_FIELD, LOGO, BUTTON_IN_MAIN
from data import TEST_EMAIL, DEFAULT_PASSWORD

def test_logo_redirect_to_main(driver):  
    
    driver.find_element(*BUTTON_IN_MAIN).click()
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(TEST_EMAIL)
    driver.find_element(*PASSWORD_FIELD).send_keys(DEFAULT_PASSWORD)
    driver.find_element(*BUTTON_IN).click()
    driver.find_element(*ACCOUNT_BUTTON).click()
    driver.find_element(*LOGO).click()

    assert driver.current_url == "https://stellarburgers.education-services.ru/"