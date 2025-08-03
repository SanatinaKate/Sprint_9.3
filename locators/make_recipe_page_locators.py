from selenium.webdriver.common.by import By
from locators.common_locators import CommonLocators


class MakeRecipePageLocators(CommonLocators):

    TITLE_CREATE_RECIPE = (By.XPATH, "//*[contains(@class, 'styles_title') and text()='Создание рецепта']")
    INPUT_TITLE = (By.XPATH, "//*[contains(@class, 'styles_inputLabelText') and text()='Название рецепта']/.."
                             "/*[contains(@class, 'styles_inputField')]")
    INPUT_TAG_CHECKBOX = (By.XPATH, "//*[text()='{}']/../*[contains(@class, 'styles_checkbox')]")
    INPUT_INGREDIENT_NAME = (By.XPATH, "//*[contains(@class, 'styles_ingredientsNameInput')]//"
                                       "*[contains(@class, 'styles_inputField')]")
    INPUT_INGREDIENT_AMOUNT = (By.XPATH, "//*[contains(@class, 'styles_ingredientsAmountInput')]//"
                                         "*[contains(@class, 'styles_inputField')]")
    INPUT_COOK_TIME = (By.XPATH, "//*[contains(@class, 'styles_inputLabelText') and text()='Время приготовления']/.."
                                 "/*[contains(@class, 'styles_inputField')]")
    INPUT_DESCRIPTION = (By.XPATH, "//*[contains(@class, 'styles_textareaLabelText') and text()='Описание рецепта']/.."
                                   "/*[contains(@class, 'styles_textareaField')]")
    INPUT_IMAGE = (By.XPATH, "//*[contains(@class, 'styles_label') and text()='Загрузить фото']/.."
                             "/*[contains(@class, 'styles_fileInput')]")
    INGREDIENT_FROM_LIST = (By.XPATH, "//*[contains(@class, 'styles_container')]/*[text()='{}']")
    BUTTON_ADD_INGREDIENT = (By.XPATH, "//*[contains(@class, 'styles_ingredientAdd') and text()='Добавить ингредиент']")
    BUTTON_CREATE_RECIPE = (By.XPATH, "//*[contains(@class, 'styles_button') and text()='Создать рецепт']")
