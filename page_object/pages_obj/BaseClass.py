import logging

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://localhost/opencart/'

    def open_url(self, url=None):
        if url is not None:
            if url.find(self.base_url) >= 0:
                self.driver.get(url)
            else:
                self.driver.get(self.base_url + url)
        else:
            self.driver.get(self.base_url)

    def find_element(self, locator_params, time=10, many_elements=False, parent_element=None):
        locator = None
        try:
            browser = self.driver
            by_selector, locator = locator_params[0], locator_params[1]
            if parent_element is not None:
                return parent_element.find_element(by_selector, locator)
            else:
                if not many_elements:
                    return WebDriverWait(browser, time).until(EC.visibility_of_element_located((by_selector,
                                                                                                locator)))
                else:
                    return browser.find_elements(by_selector, locator)
        except TimeoutException:
            return None
        except NoSuchElementException:
            return None

    def click_without_locator(self, element):
        element.click()

    def click_element(self, locator):
        self.find_element(locator).click()

    def fill_form(self, locator, text, submit_enter=False):
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(text)
        if submit_enter:
            self.find_element(locator).send_keys(Keys.ENTER)

    def verify_element(self, locator):
        assert self.find_element(locator) is not None

    def verify_url(self, url_for_check):
        url = self.driver.current_url
        assert url.find(url_for_check) >= 0

    def check_browser_log(self):
        if self.driver.name != 'firefox':
            logger = logging.getLogger('browser_log')
            logger.info('Логи браузера - начало')
            br_log = self.driver.get_log('browser')
            if br_log is not []:
                for line in br_log:
                    logger.info(line)
            logger.info('Логи браузера - конец')
