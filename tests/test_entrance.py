import time
import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils import services


class TestEntrance:

    def test_entrance_with_button_enter_in_account_on_main_page_success(self, driver):
        name, email, password = services.get_test_login()
        driver.find_element(*locators.ACCOUNT_PERSONAL_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.AUTH_LINK))
        driver.find_element(*locators.AUTH_LINK).click()
        WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(locators.REGISTRATION_BUTTON))
        driver.find_element(*locators.REGISTRATION_INPUT_NAME).send_keys(name)
        driver.find_element(*locators.REGISTRATION_INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.REGISTRATION_INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.ENTRANCE_BUTTON))
        driver.find_element(*locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.ENTRANCE_IN_ACCOUNT_BUTTON))
        driver.find_element(*locators.ENTRANCE_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.ENTRANCE_BUTTON))
        driver.find_element(*locators.ENTRANCE_INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.ENTRANCE_INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.ENTRANCE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.DO_ORDER_BUTTON))
        assert driver.find_element(*locators.DO_ORDER_BUTTON).text == "Оформить заказ"

    def test_entrance_through_personal_accaunt_success(self, driver):
        name, email, password = services.get_test_login()
        driver.find_element(*locators.ACCOUNT_PERSONAL_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.AUTH_LINK))
        driver.find_element(*locators.AUTH_LINK).click()
        WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(locators.REGISTRATION_BUTTON))
        driver.find_element(*locators.REGISTRATION_INPUT_NAME).send_keys(name)
        driver.find_element(*locators.REGISTRATION_INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.REGISTRATION_INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.ENTRANCE_BUTTON))
        driver.find_element(*locators.ENTRANCE_INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.ENTRANCE_INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.ENTRANCE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.DO_ORDER_BUTTON))
        time.sleep(5)
        assert driver.find_element(*locators.DO_ORDER_BUTTON).text == "Оформить заказ"

    def test_entrance_through_registration_form_success(self, driver):
        name, email, password = services.get_test_login()
        driver.find_element(*locators.ACCOUNT_PERSONAL_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.AUTH_LINK))
        driver.find_element(*locators.AUTH_LINK).click()
        WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(locators.REGISTRATION_BUTTON))
        driver.find_element(*locators.REGISTRATION_INPUT_NAME).send_keys(name)
        driver.find_element(*locators.REGISTRATION_INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.REGISTRATION_INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.ENTRANCE_BUTTON))
        driver.find_element(*locators.AUTH_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.REGISTRATION_BUTTON))
        driver.find_element(*locators.ENTRANCE_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.ENTRANCE_BUTTON))
        driver.find_element(*locators.ENTRANCE_INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.ENTRANCE_INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.ENTRANCE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.DO_ORDER_BUTTON))
        assert driver.find_element(*locators.DO_ORDER_BUTTON).text == "Оформить заказ"

    def test_entrance_through_password_recovery_form_success(self, driver):
        name, email, password = services.get_test_login()
        driver.find_element(*locators.ACCOUNT_PERSONAL_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.AUTH_LINK))
        driver.find_element(*locators.AUTH_LINK).click()
        WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(locators.REGISTRATION_BUTTON))
        driver.find_element(*locators.REGISTRATION_INPUT_NAME).send_keys(name)
        driver.find_element(*locators.REGISTRATION_INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.REGISTRATION_INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.ENTRANCE_BUTTON))
        driver.find_element(*locators.PASSWORD_RECOVERY_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.PASSWORD_RECOVERY_BUTTON))
        driver.find_element(*locators.ENTRANCE_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.ENTRANCE_BUTTON))
        driver.find_element(*locators.ENTRANCE_INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.ENTRANCE_INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.ENTRANCE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.DO_ORDER_BUTTON))
        assert driver.find_element(*locators.DO_ORDER_BUTTON).text == "Оформить заказ"