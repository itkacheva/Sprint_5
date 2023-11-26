from conftest import entrance_user
from urls import main_page_url
from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestGoFromPersonalAccountToConstructor:

    def test_go_from_personal_account_by_constructor_button_success(self, driver, registration_user):
        name, email, password = registration_user
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(AuthPageLocators.ENTRANCE_BUTTON))
        driver.find_element(*HeaderLocators.ACCOUNT_PERSONAL_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(AuthPageLocators.ENTRANCE_BUTTON))
        driver.find_element(*AuthPageLocators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*AuthPageLocators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*AuthPageLocators.ENTRANCE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.DO_ORDER_BUTTON))
        driver.find_element(*HeaderLocators.ACCOUNT_PERSONAL_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.INPUT_NAME))
        driver.find_element(*HeaderLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.DO_ORDER_BUTTON))
        assert driver.current_url == main_page_url

    def test_go_from_personal_account_by_logo_success(self, driver, registration_user):
        name, email, password = registration_user
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(AuthPageLocators.ENTRANCE_BUTTON))
        driver.find_element(*HeaderLocators.ACCOUNT_PERSONAL_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(AuthPageLocators.ENTRANCE_BUTTON))
        entrance_user(driver, email, password)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.DO_ORDER_BUTTON))
        driver.find_element(*HeaderLocators.ACCOUNT_PERSONAL_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.INPUT_NAME))
        driver.find_element(*HeaderLocators.LOGO).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.DO_ORDER_BUTTON))
        assert driver.current_url == main_page_url
