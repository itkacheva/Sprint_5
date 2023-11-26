from conftest import entrance_user
from urls import login_page_url
from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestExitFromPersonalAccountConstructor:

    def test_exit_from_personal_account_success(self, driver, registration_user):
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
            expected_conditions.visibility_of_element_located(ProfilePageLocators.EXIT_BUTTON))
        driver.find_element(*ProfilePageLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(AuthPageLocators.ENTRANCE_BUTTON))
        assert driver.current_url == login_page_url
