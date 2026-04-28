import pytest
from locators import BUNS_SECTION, SAUCES_SECTION,BUNS_TITLE, SAUCES_TITLE, FILLINGS_TITLE, FILLINGS_SECTION, ACCOUNT_BUTTON, LOGIN_EMAIL_FIELD, PASSWORD_FIELD, BUTTON_IN
from data import TEST_EMAIL, DEFAULT_PASSWORD
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("section_locator, section_title, section_name", [
    (SAUCES_SECTION, SAUCES_TITLE, "Соусы"),
    (FILLINGS_SECTION, FILLINGS_TITLE, "Начинки"),
    (BUNS_SECTION, BUNS_TITLE, "Булки")
])
def test_constructor_sections(driver, section_locator,section_title, section_name):
    
    driver.find_element(*ACCOUNT_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(TEST_EMAIL)
    driver.find_element(*PASSWORD_FIELD).send_keys(DEFAULT_PASSWORD)
    driver.find_element(*BUTTON_IN).click()
    driver.find_element(*section_locator).click()
    
    assert driver.find_element(*section_title).is_displayed()