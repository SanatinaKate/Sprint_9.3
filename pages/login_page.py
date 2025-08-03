import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Открыть страницу авторизации")
    def open(self):
        self.driver.get(f"{self.driver.base_url}/signin")
        self.check_element_visible(LoginPageLocators.TITLE_LOGIN)

    @allure.step("Перейти на страницу регистрации")
    def goto_register_page(self):
        self.click_element(LoginPageLocators.LINK_CREATE_ACCOUNT)
        self.check_element_invisible(LoginPageLocators.TITLE_LOGIN)

    @allure.step("Войти в аккаунт")
    def enter_account(self, user):
        self.fill_element_with_value(LoginPageLocators.INPUT_EMAIL, user['email'])
        self.fill_element_with_value(LoginPageLocators.INPUT_PASSWORD, user['password'])
        self.click_element(LoginPageLocators.BUTTON_LOGIN)
        self.check_element_invisible(LoginPageLocators.TITLE_LOGIN)

    @allure.step("Получить текст заголовка")
    def get_title_text(self):
        return self.get_element_text(LoginPageLocators.TITLE_ON_PAGE)
