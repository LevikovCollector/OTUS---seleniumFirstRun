import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='http://localhost/opencart/')
    parser.addoption('--browser', action='store', default='chrome')


@pytest.fixture
def create_driver(request):
    choose_browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    driver = None
    if choose_browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(chrome_options=options)

    elif choose_browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(firefox_binary='/home/vladimir/firefox/firefox',
                                   executable_path='/usr/local/bin/geckodriver', firefox_options=options)
    elif choose_browser == 'ie':
        raise WebDriverException('Это Linux система! Используйте chrome или firefox.')
    else:
        raise WebDriverException('Указан неверный браузер!')

    request.addfinalizer(driver.quit)
    return {'driver': driver,
            'url': url}

