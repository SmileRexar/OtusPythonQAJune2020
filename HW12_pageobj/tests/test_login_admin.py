import allure
import pytest


@allure.feature('Форма атворизация админа')
@allure.story('Вход с валидными данными')
@allure.title('Передача валиднго логин/пароля')
def test_success_login(admin_page):
    with allure.step(f"Открыть страницы страницу {admin_page.base_url}"):
        admin_page.login('user', 'bitnami')
    with allure.step(f"Проверка титула формы"):
        assert admin_page.driver.title == 'Dashboard'


@allure.feature('Форма атворизация админа')
@allure.story('Вход с невалидными данными')
@allure.title('Передача не валидного логина')
@pytest.mark.parametrize("login , passw", [
    ('user', 'bitnamibitnamibitnamibitnamibitnamibitnami'),
    ('', ''),
    (';or 1=1--', ';or 1=1--'),
    ('; логин -', ';or пасс @1=1--'),
    ('^/|--..df\\ls', ';--'),
    ('javascript:alert(‘Executed!’);', ';or 1=1--'),
    ('1', 'javascript:alert(‘Executed!’);'),
    ("<script>alert('Injected!');</script>", ''),
    ("1", "<script>alert('Injected!');</script>"),
    ("1", "<script>alert('Injected!');</script>"),
    ("1", '<html><body>  '
          '<h1>Message Board</h1>  '
          '<hr> <b>smith</b>: Hello World!<br> '
          '<form action="mb.cgi"> <input type="text" name="msg">  '
          '<input type="button" onclick="submit()" '
          'value="post message"> '
          '</form>  '
          '</body></html>'),
])
def test_negative_login(admin_page, login, passw):
    with allure.step(f"Открыть страницы страницу {admin_page.base_url}"):
        admin_page.login(login, passw)
    with allure.step(f"Проверка титула формы"):
        assert admin_page.driver.title != 'Dashboard'
