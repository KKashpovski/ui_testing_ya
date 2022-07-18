"""Test-suite for main page YA."""

import pytest


@pytest.mark.main_page_ya
class TestMainPage:
    def test_main_page_is_load(self, app):
        """
        Steps.

            1 Open main page
            2 Check YA-image.
        """
        app.open_main_page()
        assert app.main_page.page_is_load(), "Page is not load"

    def test_user_not_auth(self, app):
        """
        Steps.

            1 Open main page
            2 Check user not auth.
        """
        app.open_main_page()
        assert app.main_page.is_auth(), "Someone has already logged in to the account"

