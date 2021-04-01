import pytest
from HW12_pageobj.pages.loginpage import LoginPage


@pytest.fixture(scope="function")
def login_page(browser):
    page = LoginPage(browser)
    page.get()
    return page
