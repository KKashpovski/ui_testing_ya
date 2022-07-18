"""Test-suite for auth."""

import pytest

from common.constants import AuthConstants
from models.auth import AuthData


@pytest.mark.authorisation
class TestAuth:
    def test_auth_valid_data(self, app):
        """
        Steps.

            1 Open main page
            2 Auth with valid data
            3 Check auth result.
        """
        app.open_main_page()
        data = AuthData(login="testkks", password="kksQAZ!@#")
        app.auth_page.auth(data)
        assert app.auth_page.is_auth(), "We are not auth"

    def test_auth_invalid_login(self, app):
        """
        Steps.

            1 Open main page
            2 Auth with invalid login
            3 Check auth result.
        """
        app.open_main_page()
        data = AuthData(login="gjkgjhvkhjjg", password="fytg")
        app.auth_page.auth_with_invalid_login(data)
        assert AuthConstants.LOGIN_DOES_NOT_EXIST == app.auth_page.auth_login_error(), "We are auth!"

    def test_auth_int_login(self, app):
        """
        Steps.

            1 Open main page
            2 Auth with integer value in login
            3 Check auth result.
        """
        app.open_main_page()
        data = AuthData(login="04375868464", password="fytg")
        app.auth_page.auth_with_invalid_login(data)
        assert AuthConstants.LOGIN_IS_INT == app.auth_page.auth_login_error(), "We are auth!"

    def test_auth_empty_login(self, app):
        """
        Steps.

            1 Open main page
            2 Auth with empty login
            3 Check auth result.
        """
        app.open_main_page()
        data = AuthData(login=" ", password="fytg")
        app.auth_page.auth_with_invalid_login(data)
        assert AuthConstants.LOGIN_IS_EMPTY == app.auth_page.auth_login_error(), "We are auth!"

    @pytest.mark.parametrize("login, password",
                             [
                                 ["testkks", "fghthmjhjy"],
                                 ["testkks", "1111"],
                             ],
                             )
    def test_auth_invalid_password(self, app, login, password):
        """
        Steps.

            1 Open main page
            2 Auth with invalid password
            3 Check auth result.
        """
        app.open_main_page()
        data = AuthData(login=login, password=password)
        app.auth_page.auth_with_invalid_password(data)
        assert AuthConstants.PASS_IS_INVALID == app.auth_page.auth_pass_error(), "We are auth!"

    def test_auth_with_empty_password(self, app):
        """
        Steps.

            1 Open main page
            2 Auth with empty password
            3 Check auth result.
        """
        app.open_main_page()
        data = AuthData(login="testkks", password=None)
        app.auth_page.auth_with_invalid_password(data)
        assert AuthConstants.PASS_IS_EMPTY == app.auth_page.auth_pass_error(), "We are auth!"
