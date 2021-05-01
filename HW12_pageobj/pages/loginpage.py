from selenium.webdriver.common.by import By

from pages.base import BasePage


class LoginPage(BasePage):
    # Locator
    btn_new_user = (By.CSS_SELECTOR, '#content > div > div:nth-child(1) > div > a')
    btn_sign_user = (By.CSS_SELECTOR, '#content > div > div:nth-child(2) > div > form > input')

    # new customer
    first_name = (By.CSS_SELECTOR, '#input-firstname')
    last_name = (By.CSS_SELECTOR, '#input-lastname')
    email = (By.CSS_SELECTOR, '#input-email')
    phone = (By.CSS_SELECTOR, '#input-telephone')
    password = (By.CSS_SELECTOR, '#input-password')
    password_confirm = (By.CSS_SELECTOR, '#input-confirm')

    ch_polity_apply = (By.CSS_SELECTOR, '#content > form > div > div > input[type=checkbox]:nth-child(2)')
    btn_reg_continue = (By.CSS_SELECTOR, '#content > form > div > div > input.btn.btn-primary')

    alert_success_create = (By.CSS_SELECTOR, '#content > p:nth-child(2)')
    alert_not_sign_pair = (By.CSS_SELECTOR, '#account-login > div.alert.alert-danger.alert-dismissible')
    btn_logout_ri = (By.CSS_SELECTOR, '#column-right > div > a:nth-child(13)')
    btn_logout = (By.CSS_SELECTOR, '#content > div > div > a')
    lbl_logout_activate = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown.open > ul > li:nth-child(5) > a')

    logging_enabled = True

    def __init__(self, driver):
        super().__init__(driver, logging_enabled=self.logging_enabled)
        self.driver = driver
        self.base_url = f'{self.base_url}/index.php?route=account/login'

    def _set_registration(self):
        self.find_element(locator=self.btn_new_user).click()

    def _set_fio(self, first_name, last_name):
        self.find_element(locator=self.first_name).clear()
        self.find_element(locator=self.first_name).send_keys(first_name)
        self.find_element(locator=self.last_name).clear()
        self.find_element(locator=self.last_name).send_keys(last_name)

    def _set_email(self, email):
        self.find_element(locator=self.email).clear()
        self.find_element(locator=self.email).send_keys(email)
        print(1)

    def _set_phone(self, phone):
        self.find_element(locator=self.phone).clear()
        self.find_element(locator=self.phone).send_keys(phone)

    def _set_password(self, passwd):
        self.find_element(locator=self.password).clear()
        self.find_element(locator=self.password).send_keys(passwd)

    def _set_password_confirm(self, passwd):
        self.find_element(locator=self.password_confirm).clear()
        self.find_element(locator=self.password_confirm).send_keys(passwd)

    def _set_create_user(self):
        self.find_element(locator=self.btn_reg_continue).click()

    def _set_sign_user(self):
        self.find_element(locator=self.btn_sign_user).click()

    def _set_check_policy(self, policy):
        ch_r = self.find_element(locator=self.ch_polity_apply)
        if policy:
            ch_r.click()

    def _set_logout(self):
        self.find_element(locator=self.btn_logout_ri).click()
        self.find_element(locator=self.btn_logout).click()

    def _is_logout_active(self):
        t_ss = 0.5
        try:
            self.find_element(locator=(By.CSS_SELECTOR, '#top-links > ul > li.dropdown > a'), time=t_ss).click()
            self.find_element(locator=self.lbl_logout_activate, time=t_ss)
            return True
        except Exception as e:
            #print(e)
            return False

    def _is_not_valid_sign_in(self):
        return self.find_element(locator=(By.CSS_SELECTOR, '#account-login > div.alert.alert-danger.alert-dismissible'))

    def not_valid_sign_in(self):
        return self._is_not_valid_sign_in()

    def check_logout(self):
        return self._is_logout_active()

    def create_customer(self, first_name, last_name, email, phone, password, policy):
        self._set_registration()
        self._set_fio(first_name, last_name)
        self._set_email(email)
        self._set_phone(phone)
        self._set_password(password)
        self._set_password_confirm(password)
        self._set_check_policy(policy)
        self._set_create_user()

    def logout(self):
        self._set_logout()

    def sign_in(self, email, passwd):
        self._set_email(email)
        self._set_password(passwd)
        self._set_sign_user()