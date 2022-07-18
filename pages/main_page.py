"""Methods for main page."""


import logging

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

logger = logging.getLogger("YA")


class MainPage(BasePage):
    def is_auth(self):
        if self.find_element(MainPageLocators.CONFIRM_WINDOW):
            return True
        return False

    def page_is_load(self):
        if self.find_element(MainPageLocators.IDENTIFIC_YA):
            return True
        return False
