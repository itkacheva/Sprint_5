from faker import Faker
import random

def get_test_login():
    fake = Faker()
    name = fake.first_name()
    surname = fake.last_name()
    password = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    random_numbers = random.randint(100, 999)
    email = f"{name.lower()}_{surname.lower()}_3_{random_numbers}@yandex.com"
    return name, email, password