def test_success_login(admin_page):
    admin_page.login('user', 'bitnami')


def test_negative_login(admin_page):
    admin_page.login('', '')
    assert admin_page.driver.title != 'Dashboard'
