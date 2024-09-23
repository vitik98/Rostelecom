from page.main_page import (MainPage)
from config import TestData
import time


# Кнопка "Почта" (открывает форму входа по электронной почте)
def test_mail_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.MAIL)
    mail = main_page.is_visible(MainPage.USERNAME)
    time.sleep(2)
    assert mail == True


# Кнопка "Зарегистрироваться" (открывает форму "Регистрация")
def test_click_check_in(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    check_in = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    time.sleep(2)
    assert check_in == TestData.CHECK


# Кнопка "Забыл пароль" (открывает форму "Восстановление пароля")
def test_forgot_password(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.FORGOT)
    recovery = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    time.sleep(2)
    assert recovery == TestData.RECOVERY


# Кнопка "Вернуться назад" в форме "Восстановление пароля" (открывает форму "Авторизация")
def test_back_button(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.FORGOT)
    main_page.find_click(MainPage.BACK_BUTTON)
    auth_name = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    time.sleep(2)
    assert auth_name == TestData.AUTH