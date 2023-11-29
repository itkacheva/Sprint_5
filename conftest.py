import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from urls import main_page_url
from utils import services


def entrance_user(driver, email, password):
    driver.find_element(*AuthPageLocators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*AuthPageLocators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*AuthPageLocators.ENTRANCE_BUTTON).click()


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(main_page_url)
    yield driver
    driver.quit()


@pytest.fixture()
def registration_user(driver):
    name, email, password = services.get_test_login()
    driver.find_element(*HeaderLocators.ACCOUNT_PERSONAL_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AuthPageLocators.AUTH_LINK))
    driver.find_element(*AuthPageLocators.AUTH_LINK).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_BUTTON))
    driver.find_element(*RegistrationPageLocators.INPUT_NAME).send_keys(name)
    driver.find_element(*RegistrationPageLocators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*RegistrationPageLocators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*RegistrationPageLocators.REGISTRATION_BUTTON).click()
    return name, email, password
