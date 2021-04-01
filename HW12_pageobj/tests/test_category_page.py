def test_add_wish_without_auth(category_page):
    assert category_page.driver.title == 'Desktops'
    category_page.add_wish()
    assert 'You must login or create an account to save' in category_page.check_alert_auth()
    category_page.get()
    category_page.compare_product()
    assert 'Success: You have added' in category_page.check_alert_auth()
    category_page.get()


def test_compare_product(category_page):
    category_page.compare_product()
    assert category_page.driver.title == 'Desktops'
    category_page.get()

