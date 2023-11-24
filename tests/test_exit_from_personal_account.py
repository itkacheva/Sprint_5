from utils import services
import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestExitFromPersonalAccountConstructor:

    def test_exit_from_personal_account_success(self, driver):
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
        driver.find_element(*locators.ACCOUNT_PERSONAL_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.ENTRANCE_BUTTON))
        driver.find_element(*locators.ENTRANCE_INPUT_EMAIL).send_keys(email)
        driver.find_element(*locators.ENTRANCE_INPUT_PASSWORD).send_keys(password)
        driver.find_element(*locators.ENTRANCE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.DO_ORDER_BUTTON))
        driver.find_element(*locators.ACCOUNT_PERSONAL_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.EXIT_BUTTON))
        driver.find_element(*locators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.ENTRANCE_BUTTON))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
