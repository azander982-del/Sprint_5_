import random
import string

def generate_random_email():
    # Генерируем случайное имя из 8 букв
    name = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{name}@test.ru"

def generate_random_password():
    password = ''.join(random.choices(string.ascii_lowercase, k=6))
    return password

DEFAULT_PASSWORD = "123456"
TEST_EMAIL = "test321@test.ru"
TEST_PASSWORD = "12345"