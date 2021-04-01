def test_success_product_review(product_page):
    product_page.add_review(author='Ivan ivan', text='text for input review. Count words is 40')
    assert product_page.alert_text == 'Thank you for your review. It has been submitted to the webmaster for approval.'


def test_bad_product_review(product_page):
    product_page.add_review(author='Ivan ivan', text='text for input. Count 24')
    assert product_page.alert_text != 'Thank you for your review. It has been submitted to the webmaster for approval.'
    assert product_page.alert_text == 'Warning: Review Text must be between 25 and 1000 characters!'


def test_add_pay(product_page):
    assert 'Success: You have added' in product_page.add_to_card(10)
