import pytest
from HW12_pageobj.pages.productpage import ProductPage


@pytest.fixture(scope="function")
def product_page(browser):
    page = ProductPage(browser)
    page.get()
    return page
