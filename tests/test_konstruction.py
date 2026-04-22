import pytest
from locators import BUNS_SECTION, SAUCES_SECTION, FILLINGS_SECTION, ACCOUNT_BUTTON, LOGIN_EMAIL_FIELD, PASSWORD_FIELD, BUTTON_IN
from data import TEST_EMAIL, DEFAULT_PASSWORD
from selenium.webdriver.common.by import By
import time

@pytest.mark.parametrize("section_locator, section_name", [
    (SAUCES_SECTION, "Соусы"),
    (FILLINGS_SECTION, "Начинки"),
    (BUNS_SECTION, "Булки")
])
def test_constructor_sections(driver, section_locator, section_name):

    driver.find_element(*ACCOUNT_BUTTON).click()
    time.sleep(1)
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(TEST_EMAIL)
    driver.find_element(*PASSWORD_FIELD).send_keys(DEFAULT_PASSWORD)
    driver.find_element(*BUTTON_IN).click()
    time.sleep(1)
    
    span_element = driver.find_element(*section_locator)
    parent_div = span_element.find_element(By.XPATH, "..")
    parent_div.click()
    time.sleep(1)
    
    assert "tab_tab_type_current__2BEPc" in parent_div.get_attribute("class")