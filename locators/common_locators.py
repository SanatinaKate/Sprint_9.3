from selenium.webdriver.common.by import By


class CommonLocators:

    LINK_RECIPES = (By.XPATH, "//*[contains(@class, 'style_link') and text()='Рецепты']")
    LINK_LOGIN = (By.XPATH, "//*[contains(@class, 'style_link') and text()='Войти']")
    LINK_CREATE_ACCOUNT = (By.XPATH, "//*[contains(@class, 'style_link') and text()='Создать аккаунт']")
    TITLE_ON_PAGE = (By.XPATH, "//*[contains(@class, 'styles_title') and text()]")
    INPUT_EMAIL = (By.XPATH, "//*[contains(@class, 'styles_inputField') and @name='email']")
    INPUT_PASSWORD = (By.XPATH, "//*[contains(@class, 'styles_inputField') and @name='password']")
