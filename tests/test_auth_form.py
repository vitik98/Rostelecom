from page.main_page import (MainPage)
from config import TestData, valid_pass, valid_email, invalid_pass, invalid_email

import time


# Авторизация с корректными данными
def test_auth_mail(driver):
    main_page = MainPage(driver)
    main_page.input_keys(MainPage.USERNAME, valid_email)
    main_page.input_keys(MainPage.PASS, valid_pass)
    main_page.find_click(MainPage.BUTTON_INPUT)
    logout = main_page.is_visible(MainPage.BUTTON_LOGOUT)
    time.sleep(2)
    assert logout == True


# Авторизация с некорректным паролем
def test_invalid_auth_mail(driver):
    main_page = MainPage(driver)
    main_page.input_keys(MainPage.USERNAME, valid_email)
    main_page.input_keys(MainPage.PASS, invalid_pass)
    main_page.find_click(MainPage.BUTTON_INPUT)
    error = main_page.is_visible(MainPage.ERROR_USERNAME_PASS)
    time.sleep(2)
    assert error == True


# Авторизация с некорректным email
def test_email_invalid_auth_mail(driver):
    main_page = MainPage(driver)
    main_page.input_keys(MainPage.USERNAME, invalid_email)
    main_page.input_keys(MainPage.PASS, valid_pass)
    main_page.find_click(MainPage.BUTTON_INPUT)
    error_username = main_page.is_visible(MainPage.ERROR_USERNAME_PASS)
    time.sleep(2)
    assert error_username == True