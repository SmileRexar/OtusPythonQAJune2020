from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_page_product(browser, start_url):
    url = start_url + 'index.php?route=product/product&path=57&product_id=49'
    browser.get(url)

    # Проверка вкладок
    assert browser.find_element_by_css_selector(
        '#content > div > div.col-sm-8 > ul.nav.nav-tabs > li.active').is_enabled() == True

    browser.find_element_by_css_selector('#content > div > div.col-sm-8 > ul.nav.nav-tabs > li:nth-child(2)').click()

    # Вписать имя
    browser.find_element_by_css_selector('#input-name').send_keys('dffgghgfhrtrt')

    # Вписать отзыв
    browser.find_element_by_css_selector('#input-review').send_keys(
        'dd1sf2fd2wg21ff2gd3hfh2bg3frr3аs3rrr3ув4rr3rr3rr3rr5в3аr3rrr3srв3а3rrr')

    # Выставить рейтинг
    browser.find_element_by_css_selector(
        '#form-review > div:nth-child(5) > div > input[type=radio]:nth-child(6)').click()

    # Выбрать кнопку
    browser.find_element_by_css_selector('#button-review').click()

    # Тест не проходит без time.sleep(1) поэтому ожидание элемента
    css_select = '#form-review > div.alert.alert-success.alert-dismissible'
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, css_select)))

    actual_text = browser.find_element_by_css_selector(css_select).text
    expected_text = 'Thank you for your review. It has been submitted to the webmaster for approval.'
    assert expected_text == actual_text
