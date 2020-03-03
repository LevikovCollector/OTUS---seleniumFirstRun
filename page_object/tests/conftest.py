import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')


@pytest.fixture(scope='session')
def browser(request):
    choose_browser = request.config.getoption('--browser')
    driver = None
    if choose_browser == 'chrome':
        driver = webdriver.Chrome()

    elif choose_browser == 'firefox':
        driver = webdriver.Firefox(firefox_binary='/home/vladimir/firefox/firefox',
                                   executable_path='/usr/local/bin/geckodriver')
    elif choose_browser == 'ie':
        raise WebDriverException('Это Linux система! Используйте chrome или firefox.')
    else:
        raise WebDriverException('Указан неверный браузер!')

    request.addfinalizer(driver.quit)
    return driver
