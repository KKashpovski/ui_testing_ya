"""Basic methods for all pages."""


import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger("YA")


class BasePage:
    def __init__(self, app):
        """Construct data."""
        self.app = app

    def find_element(self, locator, wait_time=10):
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    def find_elements(self, locator):
        return self.app.driver.find_elements(*locator)

    def fill_element(self, element, text):
        element.clear()
        if text:
            element.send_keys(text)
            return element

    def click_element(self, element):
        element.click()

    def get_element_text(self, element) -> str:
        logger.info(f"Element text is: {element.text}")
        return element.text

    def switch_to_window(self):
        handles = self.app.driver.window_handles
        for handle in handles:
            if handle != self.app.driver.current_window_handle:
                logger.info(f"switch to second window {handle}")
                # self.app.driver.close()
                self.app.driver.switch_to.window(handle)

    def context_click_to_el(self, element):
        action = ActionChains(self.app.driver)
        action.context_click(on_element=element)
        action.perform()

    def double_click_to_el(self, element):
        action = ActionChains(self.app.driver)
        action.double_click(on_element=element)
        action.perform()
