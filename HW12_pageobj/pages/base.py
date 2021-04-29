import json
import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage(object):
    base_url = "http://localhost"

    def __init__(self, driver, logging_enabled: bool = False):
        self.driver = driver
        self.logging_enabled: logging_enabled

        if self.logging_enabled:
            self.handler = logging.FileHandler(filename=f"{type(self).__name__}.log")
            self.logger = logging.getLogger(name=type(self).__name__)
            self.logger.setLevel(level=logging.INFO)

    @allure.step("Поиск элемента {locator}")
    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(
                Ec.presence_of_element_located(locator),
                message=f"Can't find element by locator {locator}")
            if self.logging_enabled:
                self.logger.info(f"Найден {locator}")
            return element
        except TimeoutException:
            allure.attach(
                body=json.dumps(self.driver.capabilities, indent=4),
                name="Capabilities",
                attachment_type=allure.attachment_type.JSON
            )
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            if self.logging_enabled:
                self.logger.error(f"Не найден {locator}")
            raise TimeoutException

    @allure.step("Поиск элементов {locator}")
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            Ec.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    # @allure.step("Переход на страницу {self.base_url}")
    def get(self):
        return self.driver.get(self.base_url)
