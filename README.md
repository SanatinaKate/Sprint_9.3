Проект содержит автотесты для сервиса "Продуктовый помощник" - https://foodgram-frontend-1.prakticum-team.ru
Автотесты написаны на основе паттерна Page Object Model, с использованием фреймворков pytest и Selenium

Сами автотесты находятся в директори tests и состоят из следующих файлов:
- test_login_page.py - содержит класс TestLoginPage для проверки страницы входа
  - test_login_page_check_authorization - проверка авторизации

- test_main_page.py - содержит класс TestMainPage для проверки главной страницы
  - test_main_page_check_recipe_creation - проверка создания рецепта

- test_register_page.py - содержит класс TestRegisterPage для проверки страницы регистрации
  - test_register_page_check_account_creation - проверка создания аккаунта

В директории locators находятся файлы с локаторами страниц для автотестов:
- common_locators.py содержит класс CommonLocators с локаторами, общими для разных страниц
- login_page_locators.py содержит класс LoginPageLocators с локаторами для страницы входа
- main_page_locators.py содержит класс MainPageLocators с локаторами для главной страницы
- make_recipe_page_locators.py содержит класс MakeRecipePageLocators с локаторами для страницы создания рецепта
- register_page_locators.py содержит класс RegisterPageLocators с локаторами для страницы регистрации

В директории pages находятся файлы с методами страниц для автотестов:
- base_page.py - содержит класс BasePage с базовыми методами для всех страниц
- login_page.py - содержит класс LoginPage c методами для страницы входа
- main_page.py - содержит класс MainPage c методами для главной страницы
- make_recipe_page.py - содержит класс MakeRecipePage c методами для страницы создания рецепта
- register_page.py - содержит класс RegisterPage c методами для страницы регистрации

В директории assets находится файл burger.jpg с картинкой для автотеста проверки создания рецепта

В директории allure-report находится файл index.html с отчётом Allure о результатах запуска автотестов в браузере Chrome

Файл data.py содержит класс Data со статическими данными для автотестов

Файл helpers.ru содержит класс Helpers со статическими методами для автотестов

Файл conftest.py содержит pytest-фикстуры:
- для инициализации/закрытия веб-драйвера
- для авторизации пользователя

Файл requirements.txt содержит версии пакетов, необходимых для работы проекта

Файл Dockerfile содержит инструкции для сборки докер-образа проекта с тестами

Файл docker-compose.yml содержит конфигурацию докер-контейнеров для сборки проекта с Selenoid

Файл config.json содержит конфигурацию для докер-контейнера с браузером Chrome

В директории .github/workflows находится файл ci.yml для сборки проекта с CI/CD на базе GitHub Actions
