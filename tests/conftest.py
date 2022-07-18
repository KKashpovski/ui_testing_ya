import logging

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.application import Application
from models.auth import AuthData

logger = logging.getLogger("YA")


# @pytest.fixture(scope="session")
@pytest.fixture
def app(request):
    base_url = request.config.getoption("--base-url")
    headless_mode = request.config.getoption("--headless").lower()
    logger.info(f"Start Ya {base_url} with headless={headless_mode} mode")
    if headless_mode == "true":
        chrome_options = Options()
        chrome_options.headless = True
        fixture = Application(
            webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options),
            base_url,
        )
    elif headless_mode == "false":
        fixture = Application(
            webdriver.Chrome(ChromeDriverManager().install()),
            base_url,
        )
    else:
        raise pytest.UsageError("--headless should be true or false")
    yield fixture
    fixture.quit()


@pytest.fixture
def auth(app, request):
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    app.open_main_page()
    data = AuthData(login=username, password=password)
    app.auth_page.auth(data)
    assert app.auth_page.is_auth(), "We are not auth"
    yield
    app.cloud_page.sign_out()


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        help="enter 'true' if you want run tests in headless mode of browser,\n"
        "enter 'false' - if not",
    ),
    parser.addoption(
        "--base-url",
        action="store",
        default="http://yandex.ru",
        help="enter base_url",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="testkks",
        help="enter username",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="kksQAZ!@#",
        help="enter password",
    ),
