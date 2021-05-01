from selenium.webdriver.common.by import By

from pages.base import BasePage


class ProductPage(BasePage):

    # Вкладка Description
    review1 = (By.CSS_SELECTOR, '#content > div > div.col-sm-8 > ul.nav.nav-tabs > li.active')

    # Вкладка отзывы
    review = (By.CSS_SELECTOR, '#content > div > div.col-sm-8 > ul.nav.nav-tabs > li:nth-child(2)')
    review_name = (By.CSS_SELECTOR, '#input-name')
    review_text = (By.CSS_SELECTOR, '#input-review')
    review_rating = (By.CSS_SELECTOR, '#form-review > div:nth-child(5) > div > input[type=radio]:nth-child(6)')
    review_btn = (By.CSS_SELECTOR, '#button-review')
    success_alert_review = (By.CSS_SELECTOR, '#form-review > div.alert.alert-success.alert-dismissible')
    bad_alert_review = (By.CSS_SELECTOR, '#form-review > div.alert.alert-danger.alert-dismissible')

    # Добавление в корзину
    Qty_to_pay = (By.CSS_SELECTOR, '#input-quantity')
    btn_add_to_card = (By.CSS_SELECTOR, '#button-cart')
    alert_succes_to_pay = (By.CSS_SELECTOR, 'div.alert.alert-success.alert-dismissible')

    logging_enabled = False

    def __init__(self, driver):
        super().__init__(driver, logging_enabled=self.logging_enabled)
        
        self.driver = driver
        self.base_url = f'{self.base_url}/tablet/samsung-galaxy-tab-10-1'

    def _set_review_name(self, name):
        # self.find_element(locator=self.review).clear()
        self.find_element(locator=self.review_name).clear()
        self.find_element(locator=self.review_name).send_keys(name)

    def _set_review_text(self, text):
        self.find_element(locator=self.review_text).clear()
        self.find_element(locator=self.review_text).send_keys(text)

    def _set_rating(self):
        self.find_element(locator=self.review_rating).click()

    def _set_apply(self):
        self.find_element(locator=self.review_btn).click()

    def _set_to_pay(self, qty):
        self.find_element(locator=self.Qty_to_pay).clear()
        self.find_element(locator=self.Qty_to_pay).send_keys(qty)
        self.find_element(locator=self.btn_add_to_card).click()

    def add_review(self, author, text):
        self.find_element(locator=self.review).click()
        # имя
        self._set_review_name(author)
        # отзыв
        self._set_review_text(text)
        # rating
        self._set_rating()
        # применить
        self.find_element(locator=self.review_btn).click()
        # прроверить
        try:
            self.alert_text = self.find_element(locator=self.success_alert_review, time=1).text
        except Exception as e:
            self.alert_text = self.find_element(locator=self.bad_alert_review).text
            print(e)

    def add_to_card(self, qty):
        print(f"Добавление {qty} товаров в корзину")
        self._set_to_pay(qty)
        return self.find_element(locator=self.alert_succes_to_pay).text
