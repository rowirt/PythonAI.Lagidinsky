import logging
import datetime

# Завдання 1
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d')
current_date = datetime.date.today().strftime('%Y-%m-%d')
logging.info(f"Поточна дата: {current_date}")

# Завдання 2
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
def cause_error():
    try:
        result = 10 / 0
        return result
    except ZeroDivisionError as e:
        logging.error(f"Виникла помилка: {e}")
        return None
cause_error()

# Завдання 3
def login(username, password):
    correct_username = "user123"
    correct_password = "password456"
    assert username == correct_username and password == correct_password, "Невірне ім'я користувача або пароль"
    print("Вхід виконано успішно")

try:
    login("user123", "password456")
    login("wrong_user", "password456")
except AssertionError as e:
    print(e)
try:
    login("user123", "wrong_password")
except AssertionError as e:
    print(e)

# Завдання 4
def check_age(age):
    assert age >= 18, "Вам має бути 18 років або більше"
    print("Ви можете використовувати цей сервіс")

try:
    check_age(25)
    check_age(16)
except AssertionError as e:
    print(e)

# Завдання 5
def process_list(input_list):
    assert len(input_list) >= 3, "Список повинен містити принаймні 3 елементи"
    print(f"Список містить {len(input_list)} елементів")

my_list_long = [1, 2, 3, 4, 5]
my_list_short = [1, 2]

try:
    process_list(my_list_long)
    process_list(my_list_short)
except AssertionError as e:
    print(e)