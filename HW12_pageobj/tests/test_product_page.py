import allure


@allure.feature('Форма продукта')
@allure.story('Добавление отзыва')
@allure.title('Успешное добавление отзыва')
def test_success_product_review(product_page):
    product_page.add_review(author='Ivan ivan', text='text for input review. Count words is 40')
    assert product_page.alert_text == 'Thank you for your review. It has been submitted to the webmaster for approval.'


@allure.feature('Форма продукта')
@allure.story('Добавление отзыва')
@allure.title('Проверка валидации при добавлении отзыва')
def test_bad_product_review(product_page):
    product_page.add_review(author='Ivan ivan', text='text for input. Count 24')
    assert product_page.alert_text != 'Thank you for your review. It has been submitted to the webmaster for approval.'
    assert product_page.alert_text == 'Warning: Review Text must be between 25 and 1000 characters!'


@allure.feature('Форма продукта')
@allure.story('Добавление в корзину')
@allure.title('Добавление к оплате')
def test_add_pay(product_page):
    assert 'Success: You have added' in product_page.add_to_card(10)
