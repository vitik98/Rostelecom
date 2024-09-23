from page.main_page import (MainPage)
from config import TestData, valid_pass, valid_email, invalid_pass, invalid_email, name, surname, region, email, \
    password, false_email, false_mobile_mini, false_mobile_max, false_name_num, name_two_letters, \
    thirty_letters, thirtyone_letters
import time


# Заполнение формы "Регистрация" валидными данными и проверка кнопки "Зарегистрироваться"
def test_check_in(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, name)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    valid_reg = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    time.sleep(7)
    # assert valid_reg == TestData.VERIFICATION_EMAIL


# Заполнение формы "Регистрация" c невалидным email
def test_check_in_false_email(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, name)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, false_email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    time.sleep(7)


# Заполнение формы "Регистрация" c невалидным номером телефона (больше цифр)
def test_check_in_false_mobile_max(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, name)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, false_mobile_max)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    time.sleep(7)


# Заполнение формы "Регистрация" c невалидным номером телефона (меньше цифр)
def test_check_in_false_mobile_mini(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, name)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, false_mobile_mini)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    time.sleep(7)


# Заполнение формы "Регистрация" с невалидным именем (цифра)
def test_check_in_false_name_mini(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, false_name_num)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    time.sleep(7)


# Заполнение формы "Регистрация" с валидным именем (2 символа)
def test_check_in_name_two_letters(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, name_two_letters)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    valid_reg = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    time.sleep(7)
    # assert valid_reg == TestData.VERIFICATION_EMAIL


# Заполнение формы "Регистрация" с валидным именем (30 кириллических символов)
def test_check_in_name_thirty_letters(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, thirty_letters)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    valid_reg = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    time.sleep(7)
    # assert valid_reg == TestData.VERIFICATION_EMAIL


# Заполнение формы "Регистрация" с невалидным именем (31 кириллический символ)
def test_check_in_name_thirty_one_letters(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, thirtyone_letters)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    time.sleep(7)