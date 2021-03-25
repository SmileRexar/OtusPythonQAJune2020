import pytest


@pytest.mark.parametrize("login , passw, is_valid_pair", [
    ('user', 'bitnami', True),
    ('user', 'bitnami1', False),
    ('user', ';or 1=1--', False),
    ('user', 'bitnamibitnamibitnamibitnamibitnamibitnami', False),
    (';or 1=1--', ';or 1=1--', False),
    ('; логин -', ';or пасс @1=1--', False),
    ('^/|--..df\\ls', ';--', False),
])
def test_page_admin(browser, start_url, login, passw, is_valid_pair):
    url = start_url + 'admin/'
    browser.get(url)

    # Проверяем титл страницы
    page_title = browser.title
    assert page_title == "Administration"
    # browser.implicitly_wait(1)
    # Проверка New Customer и активности кнопки
    browser.find_element_by_css_selector('#input-username').send_keys(login)
    browser.find_element_by_css_selector('#input-password').send_keys(passw)

    browser.find_element_by_css_selector(
        '#content > div > div > div > div > div.panel-body > form > div.text-right > button').click()

    if is_valid_pair is False:
        # логин/пасс не валидные
        not_match_pair_msg = 'No match for Username and/or Password.\n×'
        assert browser.find_element_by_css_selector(
            '#content > div > div > div > div > div.panel-body > div').text == not_match_pair_msg
        return

    assert browser.title == 'Dashboard'

    # Карточка пользователя
    browser.find_element_by_css_selector('#header > div > ul > li.dropdown > a').click()
    browser.find_element_by_css_selector(
        '#header > div > ul > li.dropdown.open > ul > li:nth-child(1) > a').click()
    actual_login = browser.find_element_by_css_selector('#input-username').get_property('value')
    assert actual_login == login

    # разлогин
    browser.find_element_by_css_selector('#header > div > ul > li:nth-child(2) > a').click()
    assert browser.find_element_by_xpath(
        '//*[@id="content"]/div/div/div/div/div[1]/h1').text == 'Please enter your login details.'
