import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import allure
import os


def pytest_addoption(parser, ):
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

    wd = EventFiringWebDriver(driver, POListener())
    request.addfinalizer(wd.quit)
    allure.description('Выбран браузер: '.format(driver.name))
    return wd


class POListener(AbstractEventListener):

    def __init__(self):
        self.was_error = True

    def after_navigate_to(self, url, driver):
      with allure.step('Открывается страница: {}'.format(url)):
          self.was_error = True

    def after_find(self, by, value, driver):
       with allure.step('Поиск элемента по селектору: {}'.format(value)):
           self.was_error = True

    def after_click(self, element, driver):
        with allure.step('Клик по элементу: {}'.format(element)):
            self.was_error = True

    def on_exception(self, exception, driver):
        if self.was_error:
            allure.attach(driver.get_screenshot_as_png(), name='Ошибка', attachment_type=allure.attachment_type.PNG)
        self.was_error = False


