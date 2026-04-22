from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")  #  Кнопка Личный кабинет  
REGISTER_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']") # Кнопка Зарегистрироваться
NAME_FIELD = (By.XPATH, "(//input[@type='text'])[1]")  # Поле Имя
EMAIL_FIELD = (By.XPATH, "(//input[@type='text'])[2]")  # Поле Email
LOGIN_EMAIL_FIELD = (By.XPATH, "(//input[@type='text'])[1]")  #  Поле email на форме Войти
PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']")  # Поле пароль
REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка зарегистрироваться
BUTTON_IN = (By.XPATH, ".//button[text()='Войти']")  # Кнопка Войти
BUTTON_IN_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка Войти в акккаунт на главной странице
REGISTER_BUTTON_REG = (By.XPATH, ".//a[text()='Войти']")  # Кнопка войти на форме регистрации
BUTTON_OUT = (By.XPATH, ".//button[text()='Выход']")  # Кнопка выход
LOGO = (By.XPATH, ".//a[@href='/']")  #  logo stellar burgers
BUNS_SECTION = (By.XPATH, ".//span[text()='Булки']")  #  Меню булки
SAUCES_SECTION = (By.XPATH, ".//span[text()='Соусы']")  #  Меню Соусы
FILLINGS_SECTION = (By.XPATH, ".//span[text()='Начинки']")  #  Меню начинки
REGEN_BUTTTON = (By.XPATH, ".//a[text()='Восстановить пароль']") # Кнопка Восстановить пароль