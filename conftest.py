import pytest
from selenium import webdriver


def pytest_make_parametrize_id(val):
    return repr(val)


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    print("\nquit driver..")
    driver.quit()


