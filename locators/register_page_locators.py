from selenium.webdriver.common.by import By
from locators.common_locators import CommonLocators


class RegisterPageLocators(CommonLocators):

    TITLE_REGISTER = (By.XPATH, "//*[contains(@class, 'styles_title') and text()='Регистрация']")
    INPUT_FIRST_NAME = (By.XPATH, "//*[contains(@class, 'styles_inputField') and @name='first_name']")
    INPUT_LAST_NAME = (By.XPATH, "//*[contains(@class, 'styles_inputField') and @name='last_name']")
    INPUT_USERNAME = (By.XPATH, "//*[contains(@class, 'styles_inputField') and @name='username']")
    BUTTON_CREATE_ACCOUNT = (By.XPATH, "//*[contains(@class, 'style_button') and text()='Создать аккаунт']")
