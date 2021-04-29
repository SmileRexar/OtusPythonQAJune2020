import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


pytest_plugins = [
    "fixture.fixtures_administration_page",
    "fixture.fixtures_product_page",
    "fixture.fixtures_login_page",
    "fixture.fixtures_category_page",

]


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url_base", default="localhost")
    parser.addoption("--executor", default="localhost")
