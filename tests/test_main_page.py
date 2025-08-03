import allure
from data import Data
from pages.make_recipe_page import MakeRecipePage
from pages.main_page import MainPage


class TestMainPage:

    @allure.title("Проверка создания рецепта")
    def test_main_page_check_recipe_creation(self, login):
        main_page, make_recipe_page = MainPage(login), MakeRecipePage(login)
        main_page.goto_recipe_page()
        make_recipe_page.create(Data.RECIPE)
        assert main_page.get_recipe_card_element().is_displayed()
        assert main_page.get_recipe_title_text() == Data.RECIPE['title']
