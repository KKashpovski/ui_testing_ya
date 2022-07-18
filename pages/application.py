"""Application for app."""


import logging

from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.cloud_page import CloudPage


logger = logging.getLogger("YA")


class Application:
    def __init__(self, driver, url):
        """Construct data."""
        self.driver = driver
        self.url = url
        self.auth_page = AuthPage(self)
        self.main_page = MainPage(self)
        self.cloud_page = CloudPage(self)

    def open_main_page(self):
        """Open page."""
        self.driver.get(self.url)

    def quit(self):
        """Exit."""
        self.driver.quit()
