import uuid

from selenium import webdriver


def test_page_product(browser, start_url):
    url = start_url + 'index.php?route=account/login'
    browser.get(url)

    # Чек button New Customer
    new_customer_btn = browser.find_element_by_css_selector('#content > div > div:nth-child(1) > div > a')
    assert new_customer_btn.is_enabled()
    new_customer_btn.click()

    new_guid_client = str(uuid.uuid4())

    first_name = f'test first_name{new_guid_client}'[:31]
    last_name = f'test last name {new_guid_client}'[:31]
    email = f'{new_guid_client}@test.ru'
    phone = '1234567'
    password = 'qazqwe'

    browser.find_element_by_css_selector('#input-firstname').send_keys(first_name)
    browser.find_element_by_css_selector('#input-lastname').send_keys(last_name)
    browser.find_element_by_css_selector('#input-email').send_keys(email)
    browser.find_element_by_css_selector('#input-telephone').send_keys(phone)
    browser.find_element_by_css_selector('#input-password').send_keys(password)
    browser.find_element_by_css_selector('#input-confirm').send_keys(password)

    # check_policy
    browser.find_element_by_css_selector('#content > form > div > div > input[type=checkbox]:nth-child(2)').click()

    # Press button continue
    browser.find_element_by_css_selector('#content > form > div > div > input.btn.btn-primary').click()

    assert browser.find_element_by_css_selector('#content > h1').text == 'Your Account Has Been Created!'
    assert browser.find_element_by_css_selector(
        '#content > p:nth-child(2)').text == 'Congratulations! Your new account has been successfully created!'

    # log out
    browser.find_element_by_css_selector('#column-right > div > a:nth-child(13)').click()
    browser.find_element_by_css_selector('#content > div > div > a').click()

    # Зайти под созданным раннее пользователем
    browser.get(url)
    browser.find_element_by_css_selector('#input-email').send_keys(email)
    browser.find_element_by_css_selector('#input-email').send_keys(email)

    browser.find_element_by_css_selector('#content > div > div:nth-child(2) > div > form > input').click()
