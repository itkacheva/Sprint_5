from utils import services
import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistration:

    def test_registration_success(self, driver):
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
        driver.find_element(*locators.ACCOUNT_PERSONAL_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.PROFILE_INPUT_NAME))
        assert driver.find_element(*locators.PROFILE_INPUT_NAME).get_attribute('value') == name
        assert driver.find_element(*locators.PROFILE_INPUT_EMAIL).get_attribute('value') == email


    def test_registration_length_1_digit_get_error_wrong_password(self, driver):
        name, email, password = services.get_test_login()
        password = password[1:]
        driver.find_element(*locators.ACCOUNT_PERSONAL_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.AUTH_LINK))
        driver.find_element(*locators.AUTH_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.REGISTRATION_BUTTON))
        driver.find_element(*locators.REGISTRATION_INPUT_NAME).send_keys(name)
        driver.find_element(*locators.REGISTRATION_INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.REGISTRATION_INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.REGISTRATION_BUTTON).click()
        assert driver.find_element(*locators.REGISTRATION_INPUT_ERROR_PASSWORD).text == "Некорректный пароль"