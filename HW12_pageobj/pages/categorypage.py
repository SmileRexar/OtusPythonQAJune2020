from selenium.webdriver.common.by import By

from .base import BasePage


class CategoryPage(BasePage):
    # Пример общих элементов
    submit_button = (By.CSS_SELECTOR, 'button')
    list_view = (By.ID, 'list-view')
    grid_view = (By.ID, 'grid-view')
    sort_by = (By.ID, 'input-sort')
    sort_by_custom = (By.CSS_SELECTOR, '#input-sort > option:nth-child(4)')
    show_limit = (By.ID, 'input-limit')
    sort_by_custom = (By.CSS_SELECTOR, '#input-limit > option:nth-child(4)')

    # Локаторы конкретных товаров
    css_btn_pay = (By.CSS_SELECTOR,
                   '#content > div:nth-child(7) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(1)')
    css_btn_wish = (By.CSS_SELECTOR,
                    '#content > div:nth-child(7) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(2)')
    css_btn_compare_1 = (By.CSS_SELECTOR,
                         '#content > div:nth-child(7) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(3)')
    css_btn_compare_2 = (By.CSS_SELECTOR,
                         '#menu > div.navbar-header > button > i')
    css_alert_without_auth = (By.CSS_SELECTOR,
                              '#product-category > div.alert.alert-success.alert-dismissible')
    css_btn_compation = (By.CSS_SELECTOR,
                         '#product-category > div.alert.alert-success.alert-dismissible > a:nth-child(3)')

    logging_enabled = False

    def __init__(self, driver):
        super().__init__(driver, logging_enabled=self.logging_enabled)
        self.driver = driver
        self.base_url = f'{self.base_url}/index.php?route=product/category&path=20'

    def _set_grid_view(self):
        self.find_element(locator=self.grid_view).click()

    def _set_list_view(self):
        self.find_element(locator=self.list_view).click()

    def _set_add_wish(self):
        self.find_element(locator=self.css_btn_wish).click()

    def _set_sort(self):
        self.find_element(locator=self.sort_by_custom).click()

    def _set_show(self):
        self.find_element(locator=self.show_limit_custom).click()

    def _set_add_compare(self, css_btn_compare):
        self.find_element(locator=css_btn_compare).click()
        self.get()
        self.find_element(locator=css_btn_compare).click()

    def _comp_prod(self):
        self.find_element(locator=self.css_btn_compation, time=30).click()

    def _alert_need_auth(self):
        return self.find_element(locator=self.css_alert_without_auth).text

    def compare_product(self):
        self._set_add_compare(self.css_btn_compare_1)

    def compare_products(self):
        self._set_add_compare(self.css_btn_compare_1)
        self._set_add_compare(self.css_btn_compare_2)
        self._comp_prod()

    def set_view_on_page(self, view='list_view'):
        if view == 'list_view':
            self._set_list_view()
        if view == 'grid_view':
            self._set_grid_view()

    def set_sort(self):
        self._set_sort()

    def set_show_element_on_page(self):
        self._set_show()

    def add_wish(self):
        self._set_add_wish()

    def check_alert_auth(self):
        try:
            return self._alert_need_auth()
        except Exception as e:
            print(e)
            return None
