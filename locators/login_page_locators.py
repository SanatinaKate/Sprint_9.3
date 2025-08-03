from selenium.webdriver.common.by import By
from locators.common_locators import CommonLocators


class LoginPageLocators(CommonLocators):

    TITLE_LOGIN = (By.XPATH, "//*[contains(@class, 'styles_title') and text()='Войти на сайт']")
    BUTTON_LOGIN = (By.XPATH, "//*[contains(@class, 'style_button') and text()='Войти']")
