from selenium.webdriver.common.by import By


ACCOUNT_PERSONAL_BUTTON = (By.XPATH, ".//a[@href='/account']") # Кнопка "Личный кабинет"

AUTH_LINK = (By.XPATH, ".//a[@href='/register']") # Ссылка "зарегистрироваться"

PASSWORD_RECOVERY_BUTTON = (By.XPATH, ".//form/button[text()='Восстановить']") # Кнопка "Восстановить"

PASSWORD_RECOVERY_LINK = (By.XPATH, ".//a[@href='/forgot-password']") # Ссылка "Восстановить пароль"

REGISTRATION_BUTTON = (By.XPATH, ".//form/button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"

REGISTRATION_INPUT_NAME = (By.XPATH, ".//form/fieldset[1]//input") # Поле ввода Имени при регистрации

REGISTRATION_INPUT_EMAIL = (By.XPATH, ".//form/fieldset[2]//input") # Поле ввода email при регистрации

REGISTRATION_INPUT_PASSWORD = (By.XPATH, ".//form/fieldset[3]//input") # Поле ввода пароля при регистрации

REGISTRATION_INPUT_ERROR_PASSWORD = (By.XPATH, ".//form/fieldset[3]//div/p") # Ошибка для поля ввода пароля при регистрации

ENTRANCE_BUTTON = (By.XPATH, ".// button[text() = 'Войти']") # Кнопка "Войти" на форме входа

ENTRANCE_INPUT_EMAIL = (By.XPATH, ".//form/fieldset[1]//input") # Поле ввода email при входе

ENTRANCE_INPUT_PASSWORD = (By.XPATH, ".//form/fieldset[2]//input") # Поле ввода пароля при входе

ENTRANCE_LINK = (By.XPATH, ".//a[@href='/login']") # Ссылка "Войти" на форме регистрации

DO_ORDER_BUTTON = (By.XPATH, ".//div// button[text()='Оформить заказ']") # Кнопка "Оформить заказ"

PROFILE_INPUT_NAME = (By.XPATH, ".//div//li[1]//input") # Поле ввода Имени в профиле (в личном кабинете)

PROFILE_INPUT_EMAIL = (By.XPATH, ".//div//li[2]//input") # Поле ввода email  в профиле (в личном кабинете)

PROFILE_INPUT_PASSWORD = (By.XPATH, ".//div//li[3]//input") # Поле ввода пароля  в профиле (в личном кабинете)

CONSTRUCTOR_BUTTON = (By.XPATH, ".//li/a[@href='/']") # Кнопка "Конструктор"

LOGO = (By.XPATH, ".//nav//div//a[@href='/']") # Логотип Stellar Burgers

EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']") # Кнопка "Выход" в личном кабинете

ENTRANCE_IN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт" на главной странице

LINK_LIST_BUNS = (By.XPATH, ".//h1[text()='Соберите бургер']/../div/div[1]") # ссылка на список "Булки" на главной странице

LINK_LIST_SAUCES = (By.XPATH, ".//h1[text()='Соберите бургер']/../div/div[2]/span") # ссылка на список "Соусы" на главной странице

LINK_LIST_FILLINGS = (By.XPATH, ".//h1[text()='Соберите бургер']/../div/div[3]/span") # ссылка на список "Начинки" на главной странице

INGRIDIENT_NAME_BUNS = (By.XPATH, ".//section//div//h2[text()='Булки']") # текст "Булки" в контейнере ингридиенов для бургера

INGRIDIENT_NAME_SAUCES = (By.XPATH, ".//section//div//h2[text()='Соусы']") # текст "Соусы" в контейнере ингридиенов для бургера

INGRIDIENT_NAME_FILLINGS = (By.XPATH, ".//section//div//h2[text()='Начинки']") # текст "Начинки" в контейнере ингридиенов для бургера

INGRIDIENT_CONTAINER_BUNS = (By.XPATH, ".//section/div/div/span[text() = 'Булки']/..") # контейнер ингридиенов для булок

INGRIDIENT_CONTAINER_SAUCES = (By.XPATH, ".//section/div/div/span[text() = 'Соусы']/..") # контейнер ингридиенов для соусов

INGRIDIENT_CONTAINER_FILLINGS = (By.XPATH, ".//section/div/div/span[text() = 'Начинки']/..") # контейнер ингридиенов для начинок
