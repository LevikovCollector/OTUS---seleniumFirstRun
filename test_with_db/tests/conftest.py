import logging

import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

logging.basicConfig(level=logging.INFO, filename='test_log.log')


def pytest_addoption(parser, ):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--file', action='store', default='None')


@pytest.fixture(scope='session')
def uses_browser(request):
    return request.config.getoption('--browser')

@pytest.fixture(scope='session')
def browser(request):
    choose_browser = request.config.getoption('--browser')
    file_name = request.config.getoption('--file')
    driver = None

    driver_logger = logging.getLogger('driver_log')

    if choose_browser == 'chrome':
        driver = webdriver.Chrome()
        driver_logger.info("Открыт браузер Google Chrome")
        driver.name
    elif choose_browser == 'firefox':
        driver = webdriver.Firefox(firefox_binary='/home/vladimir/firefox/firefox',
                                   executable_path='/usr/local/bin/geckodriver')
        driver_logger.info("Открыт браузер Firefox")
        print(driver.name)
    elif choose_browser == 'ie':
        driver_logger.error('Это Linux система! Используйте chrome или firefox.')
        raise WebDriverException('Это Linux система! Используйте chrome или firefox.')
    else:
        driver_logger.error('Указан неверный браузер')
        raise WebDriverException('Указан неверный браузер!')
    wd = EventFiringWebDriver(driver, POListener(driver_logger))
    request.addfinalizer(wd.quit)

    return wd


class POListener(AbstractEventListener):

    def __init__(self, logger):
        self.logger = logger

    def after_navigate_to(self, url, driver):
        self.logger.info("Открыта страница {}".format(url))

    def after_find(self, by, value, driver):
        self.logger.info("Найден элемент '{}'".format(value))

    def after_click(self, element, driver):
        self.logger.info("Клик по элементу {}".format(element))

    def after_quit(self, driver):
        self.logger.info("Работа браузера завершена")

    def on_exception(self, exception, driver):
        self.logger.error('Возникла ошибка: {}'.format(exception))
        driver.save_screenshot('img_error/Ошибка.png')


def pytest_runtest_protocol(item, nextitem):
    item_str = str(item).split(' ')[1].replace('>', '')
    logger = logging.getLogger(item_str)
    logging.info("=**********************=")
    logger.info("===== Начало теста =====")


def pytest_runtest_teardown(item, nextitem):
    item_str = str(item).split(' ')[1].replace('>', '')
    logger = logging.getLogger(item_str)
    logger.info("===== Конец теста =====\n")
