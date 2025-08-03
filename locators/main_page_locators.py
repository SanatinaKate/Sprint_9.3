from selenium.webdriver.common.by import By
from locators.common_locators import CommonLocators


class MainPageLocators(CommonLocators):

    LINK_EXIT = (By.XPATH, "//*[contains(@class, 'styles_menuLink') and text()='Выход']")
    LINK_CREATE_RECIPE = (By.XPATH, "//*[contains(@class, 'style_link') and text()='Создать рецепт']")
    RECIPE_CARD = (By.XPATH, "//*[contains(@class, 'style_container')]/*[contains(@class, 'styles_single-card')]")
    RECIPE_TITLE = (By.XPATH, "//*[contains(@class, 'styles_single-card__title')]")
