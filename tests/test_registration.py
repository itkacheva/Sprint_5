from conftest import entrance_user
from utils import services
from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:

    def test_registration_success(self, driver, registration_user):
        name, email, password = registration_user
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(AuthPageLocators.ENTRANCE_BUTTON))
        entrance_user(driver, email, password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.DO_ORDER_BUTTON))
        driver.find_element(*HeaderLocators.ACCOUNT_PERSONAL_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.INPUT_NAME))
        assert driver.find_element(*ProfilePageLocators.INPUT_NAME).get_attribute('value') == name
        assert driver.find_element(*ProfilePageLocators.INPUT_EMAIL).get_attribute('value') == email

    def test_registration_length_1_digit_get_error_wrong_password(self, driver):
        name, email, password = services.get_test_login()
        password = password[1:]
        driver.find_element(*HeaderLocators.ACCOUNT_PERSONAL_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AuthPageLocators.AUTH_LINK))
        driver.find_element(*AuthPageLocators.AUTH_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_BUTTON))
        driver.find_element(*RegistrationPageLocators.INPUT_NAME).send_keys(name)
        driver.find_element(*RegistrationPageLocators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*RegistrationPageLocators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*RegistrationPageLocators.REGISTRATION_BUTTON).click()
        assert driver.find_element(*RegistrationPageLocators.INPUT_ERROR_PASSWORD).text == "Некорректный пароль"
