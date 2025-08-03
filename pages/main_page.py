import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Получить элемент кнопки 'Выход'")
    def get_exit_element(self):
        return self.check_element_visible(MainPageLocators.LINK_EXIT)

    @allure.step("Перейти на страницу создания рецепта")
    def goto_recipe_page(self):
        self.click_element(MainPageLocators.LINK_CREATE_RECIPE)

    @allure.step("Получить элемент карточки рецепта")
    def get_recipe_card_element(self):
        return self.check_element_visible(MainPageLocators.RECIPE_CARD)

    @allure.step("Получить название рецепта")
    def get_recipe_title_text(self):
        return self.get_element_text(MainPageLocators.RECIPE_TITLE)
