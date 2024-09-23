from page.main_page import (MainPage)
import time


# Кнопка VK, переход на форму авторизации через соц.сеть Вконтакте
def test_click_vk(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.VK)
    time.sleep(2)


# Кнопка Ok, переход на форму авторизации через соц.сеть Одноклассники
def test_click_ok(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.OK)
    time.sleep(2)


# Кнопка @, переход на форму авторизации через соц.сеть Мой мир
def test_click_mail(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.MY_WORLD)
    time.sleep(2)


# Кнопка Я, переход на форму авторизации через Яндекс
def test_click_ya(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.YA)
    main_page.find_click(MainPage.YA)
    time.sleep(2)


# Кнопка Помощь, переход на страницу Ответы на вопросы
def test_click_help(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.HELP)
    time.sleep(2)


# Кнопка Пользовательского соглашения, открывает вкладку с Публичной офертой
def test_click_Terms_of_use(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.TERMS_OF_USER)
    time.sleep(2)