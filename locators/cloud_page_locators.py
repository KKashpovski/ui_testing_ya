"""Locators for cloud page YA."""

from selenium.webdriver.common.by import By


class CloudPageLocators:
    ONBOARDING_PROMO = (By.CSS_SELECTOR, ".Base-Onboarding-Buttons-Wrapper .Base-Onboarding-Promo-Button:nth-child(2)")
    MY_FILE = (By.CSS_SELECTOR, 'div[aria-label="Файл_для_копирования.jpeg"]')
    MY_FOLDER = (By.CSS_SELECTOR, '.listing-item__title[aria-label="my_folder"]')
    ALL_FILES = (By.CSS_SELECTOR, ".listing-item_theme_tile")
    COPY_SELECTED_BUTTON = (By.CSS_SELECTOR, '.Menu-Group [value="copy"]')
    DELETE_SELECTED_BUTTON = (By.CSS_SELECTOR, 'div[value="delete"]')
    RENAME_SELECTED_BUTTON = (By.CSS_SELECTOR, '.Menu-Group [value="rename"]')
    MODAL_WIN = (By.CSS_SELECTOR, "dialog__wrap")  # окно копирования в папку
    SELECTED_FOR_COPY_FOLDER = (By.CSS_SELECTOR, '.dialog__wrap [title="my_folder"]')
    COPY_IN_MODAL_BUTTON = (By.CSS_SELECTOR, ".confirmation-dialog__footer .Button2:nth-child(2)")
    SIGN_OUT_BUTTON = (By.CSS_SELECTOR, '.legouser [aria-label="Выйти из аккаунта"]')
    USER_MENU = (By.CSS_SELECTOR, '.legouser [aria-label="Аккаунт"]')
