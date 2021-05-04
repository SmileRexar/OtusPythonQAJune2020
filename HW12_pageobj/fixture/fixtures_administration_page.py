import pytest

from pages.adminpage import AdminLoginPage


@pytest.fixture(scope="function")
def admin_page(browser):
    page = AdminLoginPage(browser)
    page.get()
    return page
