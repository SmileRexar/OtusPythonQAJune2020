import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser(request):
    url_base = request.config.getoption("--url_base")
    browser = request.config.getoption("--browser")
    if browser == 'firefox':
        driver = webdriver.Firefox()
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument("--screen-size=1200x800")
        driver = webdriver.Chrome(options=options)
    driver.get(url_base)
    yield driver
    driver.quit()


pytest_plugins = [
    "fixture.fixtures_administration_page",
    "fixture.fixtures_product_page",
    "fixture.fixtures_login_page",
    "fixture.fixtures_category_page",

]


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser for run test"
    )
    parser.addoption(
        "--url_base",
        action="store",
        default="http://localhost",
        help="path"
    )
