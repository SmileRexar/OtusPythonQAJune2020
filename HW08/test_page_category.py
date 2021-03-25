# def test_opencart_1(browser, start_url):
def test_page_category(browser, start_url):
    url = start_url + 'index.php?route=product/category&path=20'
    browser.get(url)

    # Проверка титл страницы
    page_title = browser.title
    assert page_title == "Desktops"

    # browser.implicitly_wait(1)

    # Проверка New Customer и активности кнопки
    product_pay_btn = browser.find_element_by_css_selector(
        '#content > div:nth-child(7) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(1)')
    assert product_pay_btn.is_enabled(), 'Кнопка не активна добавления в корзину'

    # Проверка активности кнопки
    product_wish_btn = browser.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/div/div[2]/div[2]/button[2]')
    assert product_wish_btn.is_enabled(), 'Кнопка добавления в wish не активна'

    # Проверка sort by
    list_sort_by = browser.find_element_by_css_selector('#input-sort')
    assert list_sort_by.is_enabled(), 'Кнопка не активна добавления в корзину'

    compare_elent = browser.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/div/div[2]/div[2]/button[3]')
    assert compare_elent.is_enabled(), 'Кнопка сравнения не активна'
