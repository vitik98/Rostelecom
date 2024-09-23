from selenium.webdriver.common.by import By
from page.base_page import BasePage
from config import TestData


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    MAIL = (By.XPATH, '//*[@id="t-btn-tab-mail"]')
    USERNAME = (By.XPATH, '// *[ @ id = "username"]')
    PASS = (By.XPATH, '//*[@id="password"]')
    BUTTON_INPUT = (By.XPATH, '//*[@id="kc-login"]')
    BUTTON_LOGOUT = (By.CSS_SELECTOR, "#logout-btn")
    ERROR_USERNAME_PASS = (By.XPATH, '// *[ @ id = "form-error-message"]')
    FORGOT = (By.CSS_SELECTOR, "#forgot_password")
    PAGE_RIGHT = (By.XPATH, '//*[@id="page-right"]/div/div/h1')
    BACK_BUTTON = (By.XPATH, '//*[@id="reset-back"]')
    REGISTER = (By.XPATH, '// *[ @ id = "kc-register"]')
    NAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input')
    SURNAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input')
    REGION = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/input')
    EMAIL = (By.XPATH, '//*[@id="address"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    PASSWORD_REPEAT = (By.XPATH, '//*[@id="password-confirm"]')
    BUTTON_REGISTER = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/button')
    VK = (By.CSS_SELECTOR, '#oidc_vk>svg')
    OK = (By.XPATH, '// *[@id="oidc_ok"]')
    MY_WORLD = (By.XPATH, '//*[@id="oidc_mail"]')
    YA = (By.XPATH, '//*[@id="oidc_ya"]')
    HELP = (By.XPATH, '//*[@id="faq-open"]/a')
    TERMS_OF_USER = (By.XPATH, '//*[@id="rt-auth-agreement-link"]')