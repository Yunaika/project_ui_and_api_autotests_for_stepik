import os
import pytest

from selene.support.shared import browser
from selenium import webdriver
from dotenv import load_dotenv
from autotest_stepik_project.framework_api.stepik import stepik_url
from autotest_stepik_project.utils.patching.allure import attach

DEFAULT_BROWSER = 'firefox'
DEFAULT_BROWSER_VERSION = '98.0'


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        default=DEFAULT_BROWSER,
        help='web: browser (chrome | firefox)'
    )

    parser.addoption(
        '--browser_version',
        default=DEFAULT_BROWSER_VERSION,
        help='web: browser version (if chrome: 100.0, 99.0; firefox: 98.0, 97.0)'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', params=['desktop', 'tablet', 'mobile'])
def window_size(request):
    return request.param

@pytest.fixture(scope='session')
def get_option_browser_name(request):
    return request.config.getoption('--browser_name')

@pytest.fixture(scope='session')
def get_option_browser_version(request):
    return request.config.getoption('--browser_version')

@pytest.fixture(scope='function')
def setup_browser(window_size, get_option_browser_name, get_option_browser_version):
    browser.config.base_url = stepik_url
    # browser.config.hold_browser_open = 'True'
    browser.config.timeout = 10

    if window_size == 'desktop':
        browser.config.window_width = 1440
        browser.config.window_height = 900
    elif window_size == 'tablet':
        browser.config.window_width = 768
        browser.config.window_height = 1024
    elif window_size == 'mobile':
        browser.config.window_width = 375
        browser.config.window_height = 667

    browser_name = get_option_browser_name
    browser_name = browser_name if browser_name != '' else DEFAULT_BROWSER

    browser_version = get_option_browser_version
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION

    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASSWORD')

    browser.config.driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        desired_capabilities=selenoid_capabilities
    )

    yield browser

    attach.html(browser)
    attach.logs(browser)
    attach.screenshot(browser)
    attach.video(browser)
    browser.quit()
