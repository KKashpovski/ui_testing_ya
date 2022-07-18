"""Methods for cloud page."""


import logging
from selenium.webdriver.remote.webelement import WebElement

from common.constants import CloudConstants
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.cloud_page_locators import CloudPageLocators

logger = logging.getLogger("YA")


class CloudPage(BasePage):
    def ya_cloud_button(self) -> WebElement:
        return self.find_element(MainPageLocators.GO_TO_CLOUD_BUTTON)

    def promo_win(self) -> WebElement:
        return self.find_element(CloudPageLocators.ONBOARDING_PROMO)

    def go_to_ya_cloud(self):
        self.click_element(self.ya_cloud_button())
        self.switch_to_window()
        # self.click_element(self.promo_win())

    def my_file(self) -> WebElement:
        return self.find_element(CloudPageLocators.MY_FILE)

    def my_folder(self) -> WebElement:
        return self.find_element(CloudPageLocators.MY_FOLDER)

    def copy_button(self) -> WebElement:
        return self.find_element(CloudPageLocators.COPY_SELECTED_BUTTON)

    def selected_folder(self) -> WebElement:
        return self.find_element(CloudPageLocators.SELECTED_FOR_COPY_FOLDER)

    def copy_submit_button(self) -> WebElement:
        return self.find_element(CloudPageLocators.COPY_IN_MODAL_BUTTON)

    def copy_file(self):
        self.context_click_to_el(self.my_file())
        self.click_element(self.copy_button())
        self.click_element(self.selected_folder())
        self.click_element(self.copy_submit_button())

    def open_folder(self):
        self.double_click_to_el(self.my_folder())
        self.find_element(CloudPageLocators.MY_FILE, 5)

    def delete_button(self) -> WebElement:
        return self.find_element(CloudPageLocators.DELETE_SELECTED_BUTTON)

    def del_files(self):
        items = self.find_elements(CloudPageLocators.ALL_FILES)
        for i in items:
            res = self.get_element_text(i)
            if res == self.get_file_name():
                pass
            else:
                self.context_click_to_el(i)
                self.click_element(self.delete_button())

    def my_file_in_folder(self):
        if self.find_element(CloudPageLocators.MY_FILE):
            return True
        else:
            return False

    def get_file_name(self) -> str:
        el_attr = self.get_element_text(self.my_file())
        return el_attr

    def user_menu(self) -> WebElement:
        return self.find_element(CloudPageLocators.USER_MENU)

    def exit(self) -> WebElement:
        return self.find_element(CloudPageLocators.SIGN_OUT_BUTTON)

    def sign_out(self):
        self.click_element(self.user_menu())
        self.click_element(self.exit())
