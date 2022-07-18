"""Locators for main page YA."""

from selenium.webdriver.common.by import By


class AuthPageLocators:
    LOGIN_FIELD = (By.ID, "passp-field-login")
    PASSWORD_FIELD = (By.ID, "passp-field-passwd")
    SIGN_IN_BUTTON = (By.ID, "passp:sign-in")
    NEGATIVE_LOGIN_HINT = (By.ID, "field:input-login:hint")
    NEGATIVE_PASS_HINT = (By.ID, "field:input-passwd:hint")
