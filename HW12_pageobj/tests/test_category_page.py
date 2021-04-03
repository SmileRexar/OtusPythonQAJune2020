import allure


@allure.feature('Проверка формы категории')
@allure.story('Добавление в wish лист')
@allure.title('Не авторизиранный пользователь')
def test_add_wish_without_auth(category_page):
    with allure.step(f"Добавление в wish лист"):
        assert category_page.driver.title == 'Desktops'
        category_page.add_wish()
        assert 'You must login or create an account to save' in category_page.check_alert_auth()
    with allure.step(f"Добавление в сравнение"):
        category_page.get()
        category_page.compare_product()
        assert 'Success: You have added' in category_page.check_alert_auth()
        category_page.get()


@allure.feature('Проверка формы категории')
@allure.story('Добавление в wish лист')
@allure.title('При разных сортировках и отображениях')
def test_category_sort(category_page):
    with allure.step(f"Выбор сортировки на форме"):
        category_page.set_sort()
    with allure.step(f"Отображения через grid на форме"):
        category_page.set_view_on_page()
    with allure.step(f"Выбор кол-во элементов на форме"):
        category_page.set_show_element_on_page
    with allure.step(f"Добавление в wish лист"):
        assert category_page.driver.title == 'Desktops'
        category_page.add_wish()
        assert 'You must login or create an account to save' in category_page.check_alert_auth()


