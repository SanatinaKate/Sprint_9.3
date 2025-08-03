import allure
from data import Data
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.register_page import RegisterPage


class TestLoginPage:

    @allure.title("Проверка авторизации")
    def test_login_page_check_authorization(self, driver):
        login_page, main_page, register_page = LoginPage(driver), MainPage(driver), RegisterPage(driver)
        register_page.open()
        register_page.goto_login_page()
        login_page.enter_account(Data.USER)
        assert "/recipes" in main_page.get_current_url()
        assert main_page.get_exit_element().is_displayed()
