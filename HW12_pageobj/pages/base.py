from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    base_url = "http://localhost"

    def __init__(
            self,
            driver,
    ):        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            Ec.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            Ec.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    def get(self):
        return self.driver.get(self.base_url)
