"""Locators for main page YA."""

from selenium.webdriver.common.by import By


class MainPageLocators:
    IDENTIFIC_YA = (By.CSS_SELECTOR, ".home-logo__default[role=img]")
    CONFIRM_WINDOW = (By.CSS_SELECTOR, ".desk-notif-card__login-new-items")
    # CLI_NOT_AUTH = (By.CSS_SELECTOR, ".home-link.desk-notif-card__login-new-item.desk-notif-card__login-new-item_enter.home-link_black_yes.home-link_hover_inherit")
    CLI_NOT_AUTH = (By.CSS_SELECTOR, 'a[data-statlog="notifications.mail.logout.enter"]')
    # CLI_IS_AUTH = (By.CSS_SELECTOR, ".desk-notif-card__domik-user.usermenu-link.i-bem")
    CLI_IS_AUTH = (By.CSS_SELECTOR, '.usermenu-link a[aria-haspopup="true"]')
    # GO_TO_CLOUD_BUTTON = (By.CSS_SELECTOR, ".desk-notif-card__toggled > .desk-notif-card__domik-item > .home-link.home-link_black_yes")
    GO_TO_CLOUD_BUTTON = (By.CSS_SELECTOR, ".desk-notif-card__toggled .desk-notif-card__domik-item .home-link.home-link_black_yes")
    SIGN_OUT_BUTTON = (By.CSS_SELECTOR, '.usermenu [aria-label="Выйти"]')
