import allure
from helpers import Helpers
from locators.make_recipe_page_locators import MakeRecipePageLocators
from pages.base_page import BasePage


class MakeRecipePage(BasePage):

    @allure.step("Создать рецепт")
    def create(self, data):
        self.check_element_visible(MakeRecipePageLocators.TITLE_CREATE_RECIPE)
        self.fill_element_with_value(MakeRecipePageLocators.INPUT_TITLE, data['title'])
        for tag in ("Завтрак", "Обед", "Ужин"):
            if tag not in data['tags']:
                locator = self.get_locator_with_value(MakeRecipePageLocators.INPUT_TAG_CHECKBOX, tag)
                self.click_element(locator)
        for ingredient in data['ingredients']:
            self.fill_element_with_value(MakeRecipePageLocators.INPUT_INGREDIENT_NAME, ingredient[0])
            locator = self.get_locator_with_value(MakeRecipePageLocators.INGREDIENT_FROM_LIST, ingredient[0])
            self.click_element(locator)
            self.fill_element_with_value(MakeRecipePageLocators.INPUT_INGREDIENT_AMOUNT, ingredient[1])
            self.click_element(MakeRecipePageLocators.BUTTON_ADD_INGREDIENT)
        self.fill_element_with_value(MakeRecipePageLocators.INPUT_COOK_TIME, data['cook_time'])
        self.fill_element_with_value(MakeRecipePageLocators.INPUT_DESCRIPTION, data['description'])
        image_path = f"{Helpers.get_root_dir()}/assets/{data['image']}"
        self.fill_element_with_value(MakeRecipePageLocators.INPUT_IMAGE, image_path, False)
        self.click_element(MakeRecipePageLocators.BUTTON_CREATE_RECIPE)
        self.check_element_invisible(MakeRecipePageLocators.TITLE_CREATE_RECIPE)
