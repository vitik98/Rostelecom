valid_email = ""
valid_pass = ""

invalid_email = 'mail@mai.com'
invalid_pass = '11111'

name = 'Иван'
surname = 'Иванов'
region = 'Москва г'
email = 'ivanovivan123@gmail.com'
password = 'A2345678'

false_email = 'майл@gmail,ru'
false_mobile_max = '8900123123123'
false_mobile_mini = '890012312'
false_name_num = '1'
name_two_letters = "Аб"
thirty_letters = 'Абвгдежзиклмнопртсуфхцчшщъыьэю'
thirtyone_letters = 'Абвгдежзиклмнопртсуфхцчшщъыьэюя'

class TestData:
    BASE_URL = 'https://b2c.passport.rt.ru/'

    FORM_AUTH_MAIL = 'Почта'
    AUTH = 'Авторизация'
    RECOVERY = 'Восстановление пароля'
    CHECK = 'Регистрация'
    VERIFICATION_EMAIL = 'Подтверждение email'
    VERIFICATION_INVALID_EMAIL = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    VERIFICATION_INVALID_NAME = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
