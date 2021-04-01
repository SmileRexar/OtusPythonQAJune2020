import pytest
from HW12_pageobj.pages.categorypage import CategoryPage


@pytest.fixture(scope="function")
def category_page(browser):
    page = CategoryPage(browser)
    page.get()
    return page
