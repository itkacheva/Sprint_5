from conftest import entrance_user
from urls import profile_page_url
from locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestGoToPersonalAccount:

    def test_go_to_personal_account_by_click_button_personal_account_success(self, driver, registration_user):
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
        assert driver.current_url == profile_page_url
