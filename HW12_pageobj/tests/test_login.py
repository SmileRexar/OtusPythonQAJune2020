import uuid

import allure


@allure.feature('Проверка формы логина')
@allure.story('Вход пользователя')
@allure.title('Создание и вход пользователя')
def test_create_customer_and_sign_in(login_page):
    with allure.step(f"Генераци данных юзера"):
        new_guid_client = str(uuid.uuid4())
        first_name = f'test first_name{new_guid_client}'[:31]
        last_name = f'test last name {new_guid_client}'[:31]
        email = f'{new_guid_client}@test.ru'
        phone = '1234567'
        password = 'qazqwe'
        policy = True
    with allure.step(f"Создание пользователя"):
        login_page.create_customer(first_name, last_name, email, phone, password, policy)
        assert login_page.driver.title == 'Your Account Has Been Created!'
        assert login_page.check_logout() is True, 'Клиент не залоген'
    with allure.step(f"Выход из системы"):
        login_page.logout()
        assert login_page.check_logout() is False, 'Клиент не разлогинен'
    with allure.step(f"Вход под ранее созданным"):
        login_page.get()
        login_page.sign_in(email, password)
        assert login_page.check_logout() is True, 'Клиент не разлогинен'
        login_page.logout()
        assert login_page.check_logout() is False, 'Клиент не разлогинен'
        login_page.get()


@allure.feature('Проверка формы логина')
@allure.story('Вход пользователя')
@allure.title('Вход не валидным пользователем')
def test_not_valid_sign_in_client(login_page):
    with allure.step(f"Генераци данных юзера"):
        new_guid_client = str(uuid.uuid4())
        email = f'{new_guid_client}@test.ru'
        password = 'qazqwe'
    with allure.step(f"Вход в систему"):
        login_page.sign_in(email, password)
        result = login_page.not_valid_sign_in().text
        assert result == 'Warning: No match for E-Mail Address and/or Password.'
        assert login_page.check_logout() is False, 'Клиент не разлогинен'
        login_page.get()
