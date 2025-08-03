import pytest
from data import Data
from selenium import webdriver
from pages.login_page import LoginPage


# Фикстура для инициализации/закрытия веб-драйвера
@pytest.fixture(params=["remote"])
def driver(request):
    if request.param == "local":
        driver = webdriver.Chrome()
    else:
        options = webdriver.ChromeOptions()
        driver = webdriver.Remote(command_executor="http://selenoid:4444/wd/hub", options=options)
    driver.set_window_size(1920, 1080)
    driver.base_url = Data.BASE_URL
    driver.timeout = 5
    yield driver
    driver.quit()

# Фикстура для авторизации пользователя
@pytest.fixture
def login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_account(Data.USER)
    return driver
