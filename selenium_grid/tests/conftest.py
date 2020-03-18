import logging

import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

logging.basicConfig(level=logging.INFO, filename='test_log.log')


def pytest_addoption(parser, ):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--remote', action='store_true', default=True)
    parser.addoption('--br_remote', action='store_true', default=False)
    parser.addoption('--selenoid', action='store_true', default=True)

@pytest.fixture(scope='session')
def browser(request):
    choose_browser = request.config.getoption('--browser')
    driver = None
    remote_flag = request.config.getoption('--remote')
    br_remote = request.config.getoption('--br_remote')
    selenoid_flag = request.config.getoption('--selenoid')
    driver_logger = logging.getLogger('driver_log')

    if remote_flag:
        if selenoid_flag:
            capabilities = {
                "browserName": "opera",
                "version": "65.0",
                "enableVNC": True,
                "enableVideo": False
            }

            driver = webdriver.Remote(
                command_executor="http://192.168.1.72:4444/wd/hub/",
                desired_capabilities=capabilities)

        elif br_remote:
            desired_cap = {
                'browser': 'Opera',
                'browser_version': '12.16',
                'os': 'Windows',
                'os_version': '7',
                'resolution': '1024x768',
                'name': 'Bstack-[Python] Sample Test'
            }
            driver = webdriver.Remote(
                command_executor='http://bsuser64205:v3DG6ygvvXiDj9ZdgUXs@hub.browserstack.com:80/wd/hub',
                desired_capabilities=desired_cap)
        else:
            driver = webdriver.Remote(command_executor="http://192.168.1.72:4444/wd/hub",
                                      desired_capabilities={'browserName': choose_browser})
    else:
        if choose_browser == 'chrome':
            driver = webdriver.Chrome()
            driver_logger.info("Открыт браузер Google Chrome")
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
