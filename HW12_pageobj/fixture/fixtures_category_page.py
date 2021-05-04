import pytest

from pages.categorypage import CategoryPage


@pytest.fixture(scope="function")
def category_page(browser):
    page = CategoryPage(browser)
    page.get()
    return page
