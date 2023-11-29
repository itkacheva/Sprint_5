from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import entrance_user


class TestEntrance:

    def test_entrance_with_button_enter_in_account_on_main_page_success(self, driver, registration_user):
        name, email, password = registration_user
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(AuthPageLocators.ENTRANCE_BUTTON))
        driver.find_element(*HeaderLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.ENTRANCE_IN_ACCOUNT_BUTTON))
        driver.find_element(*MainPageLocators.ENTRANCE_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(AuthPageLocators.ENTRANCE_BUTTON))
        entrance_user(driver, email, password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.DO_ORDER_BUTTON))
        assert driver.find_element(*MainPageLocators.DO_ORDER_BUTTON).text == "Оформить заказ"

    def test_entrance_through_personal_account_success(self, driver, registration_user):
        name, email, password = registration_user
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(AuthPageLocators.ENTRANCE_BUTTON))
        entrance_user(driver, email, password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.DO_ORDER_BUTTON))
        assert driver.find_element(*MainPageLocators.DO_ORDER_BUTTON).text == "Оформить заказ"

    def test_entrance_through_registration_form_success(self, driver, registration_user):
        name, email, password = registration_user
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(AuthPageLocators.ENTRANCE_BUTTON))
        driver.find_element(*AuthPageLocators.AUTH_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_BUTTON))
        driver.find_element(*RegistrationPageLocators.ENTRANCE_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(AuthPageLocators.ENTRANCE_BUTTON))
        entrance_user(driver, email, password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.DO_ORDER_BUTTON))
        assert driver.find_element(*MainPageLocators.DO_ORDER_BUTTON).text == "Оформить заказ"

    def test_entrance_through_password_recovery_form_success(self, driver, registration_user):
        name, email, password = registration_user
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(AuthPageLocators.ENTRANCE_BUTTON))
        driver.find_element(*AuthPageLocators.PASSWORD_RECOVERY_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(RecoveryPageLocators.PASSWORD_RECOVERY_BUTTON))
        driver.find_element(*RegistrationPageLocators.ENTRANCE_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(AuthPageLocators.ENTRANCE_BUTTON))
        entrance_user(driver, email, password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.DO_ORDER_BUTTON))
        assert driver.find_element(*MainPageLocators.DO_ORDER_BUTTON).text == "Оформить заказ"
