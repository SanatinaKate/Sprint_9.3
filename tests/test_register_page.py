import allure
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


class TestRegisterPage:

    @allure.title("Проверка создания аккаунта")
    def test_register_page_check_account_creation(self, driver):
        login_page, register_page = LoginPage(driver), RegisterPage(driver)
        login_page.open()
        login_page.goto_register_page()
        register_page.create_account()
        assert "/signin" in login_page.get_current_url()
        assert "Войти на сайт" == login_page.get_title_text()
