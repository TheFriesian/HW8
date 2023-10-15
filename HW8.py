'''
Написати валідації за допомогою регулярних виразів:
- домашній номер телефону (тільки цифри та довжина номера)
'''
import re

def validate_home_phone(phone):
    pattern = r"^\d{6,10}$"
    return bool(re.match(pattern, phone))

print(validate_home_phone("123456"))

'''
- Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
'''
def validate_mobile_phone(phone):
    pattern = r"^\+?\d{10,13}$"
    return bool(re.match(pattern, phone))

print(validate_mobile_phone("1234567890"))

'''
- email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
'''
def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email)) and (5 <= len(email) <= 50)

print(validate_email("test.name@email.co.uk"))

'''
- ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
'''
def validate_full_name(name):
    pattern = r"^[\wА-Яа-яЇїІіЄєҐґ]{2,20} [\wА-Яа-яЇїІіЄєҐґ]{2,20} [\wА-Яа-яЇїІіЄєҐґ]{2,20}$"
    return bool(re.match(pattern, name))

print(validate_full_name("Фединяк Любомир Михайлович"))
'''
- Пароль (мінімально: одна велика літера, одна маленька літера, одна цифра, один символ, довжина пароля –
 від 8 до 16 символів)
'''
def validate_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$"
    return bool(re.match(pattern, password))
print(validate_password("Password1@"))