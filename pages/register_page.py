import allure
from helpers import Helpers
from locators.register_page_locators import RegisterPageLocators
from pages.base_page import BasePage


class RegisterPage(BasePage):

    @allure.step("Открыть страницу регистрации")
    def open(self):
        self.driver.get(f"{self.driver.base_url}/signup")
        self.check_element_visible(RegisterPageLocators.TITLE_REGISTER)

    @allure.step("Перейти на страницу авторизации")
    def goto_login_page(self):
        self.click_element(RegisterPageLocators.LINK_LOGIN)
        self.check_element_invisible(RegisterPageLocators.TITLE_REGISTER)

    @allure.step("Создать аккаунт")
    def create_account(self, user=None):
        user_data = Helpers.generate_random_user() if user is None else dict(user)
        self.check_element_visible(RegisterPageLocators.TITLE_REGISTER)
        self.fill_element_with_value(RegisterPageLocators.INPUT_FIRST_NAME, user_data['first_name'])
        self.fill_element_with_value(RegisterPageLocators.INPUT_LAST_NAME, user_data['last_name'])
        self.fill_element_with_value(RegisterPageLocators.INPUT_USERNAME, user_data['username'])
        self.fill_element_with_value(RegisterPageLocators.INPUT_EMAIL, user_data['email'])
        self.fill_element_with_value(RegisterPageLocators.INPUT_PASSWORD, user_data['password'])
        self.click_element(RegisterPageLocators.BUTTON_CREATE_ACCOUNT)
        self.check_element_invisible(RegisterPageLocators.TITLE_REGISTER)
        return user_data
