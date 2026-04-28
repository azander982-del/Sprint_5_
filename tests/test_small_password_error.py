from locators import ACCOUNT_BUTTON, REGISTER_LINK, NAME_FIELD, EMAIL_FIELD, PASSWORD_FIELD, REGISTER_BUTTON
from data import generate_random_email, TEST_PASSWORD
from selenium.webdriver.common.by import By

def test_registration_short_password_error(driver):
    
    driver.find_element(*ACCOUNT_BUTTON).click()
    driver.find_element(*REGISTER_LINK).click()
    driver.find_element(*NAME_FIELD).send_keys("Тестовый пользователь")
    driver.find_element(*EMAIL_FIELD).send_keys(generate_random_email())
    driver.find_element(*PASSWORD_FIELD).send_keys(TEST_PASSWORD)
    driver.find_element(*REGISTER_BUTTON).click()
    
    assert driver.find_element(By.XPATH, ".//p[text()='Некорректный пароль']").is_displayed()