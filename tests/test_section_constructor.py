import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class TestSectionConstructor:

    def test_go_to_list_buns_success(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LINK_LIST_BUNS))
        driver.find_element(*locators.LINK_LIST_SAUCES).click()
        driver.find_element(*locators.LINK_LIST_BUNS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LINK_LIST_BUNS))
        assert 'tab_tab_type_current' in (driver.find_element(*locators.INGRIDIENT_CONTAINER_BUNS).get_attribute('class'))

    def test_go_to_list_sauces_success(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LINK_LIST_BUNS))
        driver.find_element(*locators.LINK_LIST_SAUCES).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LINK_LIST_SAUCES))
        assert 'tab_tab_type_current' in (driver.find_element(*locators.INGRIDIENT_CONTAINER_SAUCES).get_attribute('class'))

    def test_go_to_list_fillings_success(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LINK_LIST_BUNS))
        driver.find_element(*locators.LINK_LIST_FILLINGS).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.LINK_LIST_FILLINGS))
        assert 'tab_tab_type_current' in (driver.find_element(*locators.INGRIDIENT_CONTAINER_FILLINGS).get_attribute('class'))
