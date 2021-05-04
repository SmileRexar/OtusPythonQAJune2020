import pytest

from pages.productpage import ProductPage


@pytest.fixture(scope="function")
def product_page(browser):
    page = ProductPage(browser)
    page.get()
    return page
