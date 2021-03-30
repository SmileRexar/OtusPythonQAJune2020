from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_opencart(browser, start_url):
    browser.get(start_url)
    # Проверяем титл страницы
    page_title = browser.title
    assert page_title == "Your Store"
    # browser.implicitly_wait(1)
    page_open_card = browser.find_element_by_css_selector("body > footer > div > p > a").text
    assert page_open_card == 'OpenCart'

    # browser.find_element_by_css_selector('body > footer > div > div > div:nth-child(1) > ul > li:nth-child(1) > a').click()
    js_button = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "body > footer > div > div > div:nth-child(1) > ul > li:nth-child(1) > a")))
    js_button.click()
