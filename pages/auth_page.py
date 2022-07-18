"""Methods for auth page."""


import logging

from selenium.webdriver.remote.webelement import WebElement
from models.auth import AuthData
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.auth_page_locators import AuthPageLocators

logger = logging.getLogger("YA")


class AuthPage(BasePage):
    def is_auth(self):
        if self.find_element(MainPageLocators.CLI_IS_AUTH):
            return True
        return False

    def login_input(self) -> WebElement:
        return self.find_element(AuthPageLocators.LOGIN_FIELD)

    def password_input(self) -> WebElement:
        return self.find_element(AuthPageLocators.PASSWORD_FIELD)

    def submit_button(self) -> WebElement:
        return self.find_element(AuthPageLocators.SIGN_IN_BUTTON)

    def user_menu(self) -> WebElement:
        return self.find_element(MainPageLocators.CLI_IS_AUTH)

    def exit(self) -> WebElement:
        return self.find_element(MainPageLocators.SIGN_OUT_BUTTON)

    def confirm_menu(self):
        return self.find_element(MainPageLocators.CONFIRM_WINDOW)

    def log_in_button(self) -> WebElement:
        return self.find_element(MainPageLocators.CLI_NOT_AUTH)

    def auth(self, data: AuthData):
        logger.info(f'User login is "{data.login}, user password {data.password}"')
        self.click_element(self.log_in_button())
        self.fill_element(self.login_input(), data.login)
        self.click_element(self.submit_button())
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.submit_button())

    def auth_with_invalid_login(self, data: AuthData):
        logger.info(f'User login is "{data.login}"')
        self.click_element(self.log_in_button())
        self.fill_element(self.login_input(), data.login)
        self.click_element(self.submit_button())

    def auth_with_invalid_password(self, data: AuthData):
        logger.info(f'User login is "{data.login}, user password {data.password}"')
        self.click_element(self.log_in_button())
        self.fill_element(self.login_input(), data.login)
        self.click_element(self.submit_button())
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.submit_button())

    def auth_login_error(self) -> str:
        return self.find_element(AuthPageLocators.NEGATIVE_LOGIN_HINT).text

    def auth_pass_error(self) -> str:
        return self.find_element(AuthPageLocators.NEGATIVE_PASS_HINT).text

    def sign_out(self):
        self.click_element(self.user_menu())
        self.click_element(self.exit())
