from selenium.webdriver.common.by import By


class HeaderLocators:
    ACCOUNT_PERSONAL_BUTTON = (By.XPATH, ".//a[@href='/account']")  # Кнопка "Личный кабинет"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//li/a[@href='/']")  # Кнопка "Конструктор"
    LOGO = (By.XPATH, ".//nav//div//a[@href='/']")  # Логотип Stellar Burgers


class AuthPageLocators:
    AUTH_LINK = (By.XPATH, ".//a[@href='/register']")  # Ссылка "зарегистрироваться"
    PASSWORD_RECOVERY_LINK = (By.XPATH, ".//a[@href='/forgot-password']")  # Ссылка "Восстановить пароль"
    ENTRANCE_BUTTON = (By.XPATH, ".// button[text() = 'Войти']")  # Кнопка "Войти" на форме входа
    INPUT_EMAIL = (By.XPATH, ".//form/fieldset[1]//input")  # Поле ввода email при входе
    INPUT_PASSWORD = (By.XPATH, ".//form/fieldset[2]//input")  # Поле ввода пароля при входе


class RegistrationPageLocators:
    REGISTRATION_BUTTON = (By.XPATH, ".//form/button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    INPUT_NAME = (By.XPATH, ".//form/fieldset[1]//input")  # Поле ввода Имени при регистрации
    INPUT_EMAIL = (By.XPATH, ".//form/fieldset[2]//input")  # Поле ввода email при регистрации
    INPUT_PASSWORD = (By.XPATH, ".//form/fieldset[3]//input")  # Поле ввода пароля при регистрации
    INPUT_ERROR_PASSWORD = (By.XPATH, ".//form/fieldset[3]//div/p")  # Ошибка для поля ввода пароля при регистрации
    ENTRANCE_LINK = (By.XPATH, ".//a[@href='/login']")  # Ссылка "Войти" на форме регистрации


class RecoveryPageLocators:
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, ".//form/button[text()='Восстановить']")  # Кнопка "Восстановить"


class ProfilePageLocators:
    INPUT_NAME = (By.XPATH, ".//div//li[1]//input")  # Поле ввода Имени в профиле (в личном кабинете)
    INPUT_EMAIL = (By.XPATH, ".//div//li[2]//input")  # Поле ввода email  в профиле (в личном кабинете)
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # Кнопка "Выход" в личном кабинете


class MainPageLocators:
    DO_ORDER_BUTTON = (By.XPATH, ".//div// button[text()='Оформить заказ']")  # Кнопка "Оформить заказ"
    ENTRANCE_IN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    LINK_LIST_BUNS = (By.XPATH, ".//h1[text()='Соберите бургер']/../div/div[1]")  # ссылка на список "Булки"
    LINK_LIST_SAUCES = (By.XPATH, ".//h1[text()='Соберите бургер']/../div/div[2]/span")  # ссылка на список "Соусы"
    LINK_LIST_FILLINGS = (By.XPATH, ".//h1[text()='Соберите бургер']/../div/div[3]/span")  # ссылка на список "Начинки"
    CONTAINER_BUNS = (By.XPATH, ".//section/div/div/span[text() = 'Булки']/..")  # контейнер ингридиенов для булок
    CONTAINER_SAUCES = (By.XPATH, ".//section/div/div/span[text() = 'Соусы']/..")  # контейнер ингридиенов для соусов
    CONTAINER_FILLINGS = (By.XPATH, ".//section/div/div/span[text() = 'Начинки']/..")  # контейнер ингридиенов для начинок
