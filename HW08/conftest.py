import pytest
from selenium import webdriver


# @pytest.fixture
# def chrome_browser():
#     options = webdriver.ChromeOptions()
#     # options.add_argument("headless")
#     wd = webdriver.Chrome(options=options)
#     yield wd
#     wd.quit()
#
#
# @pytest.fixture
# def firefox_browser():
#     wd = webdriver.Firefox()
#     yield wd
#     wd.quit()


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")

    if browser == 'firefox':
        wd = webdriver.Firefox()
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        wd = webdriver.Chrome(options=options)
    yield wd
    wd.quit()


@pytest.fixture(scope="module")
def start_url(request):
    return request.config.getoption("--url")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="http://127.0.0.1/",
        help="Request base url for opencart"
    )
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        help="Browser for run test"
    )
