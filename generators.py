import random
import string

def generate_email():
    return f"vera_vazhdaeva_32_{''.join(random.choices(string.digits, k=3))}@yandex.ru"

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
