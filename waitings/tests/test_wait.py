from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium_grid.locators import ProductPage


def test_product_page(browser, user_time):
    '''Проверяем элементы страницы выбранного продукта'''
    browser.implicitly_wait(user_time)
    browser.get('http://localhost/opencart/')

    element = find_element_with_time(browser, user_time, "div[class='product-thumb transition']>div[class='image']>a")
    element.click()

    find_element_with_time(browser, user_time, ProductPage.PRODUCT_PRICE)
    find_element_with_time(browser, user_time, ProductPage.PRODUCT_DESCRIPTION)
    find_element_with_time(browser, user_time, ProductPage.ADD_PRODUCT_BUTTON)
    find_element_with_time(browser, user_time, ProductPage.WISH_LIST_BUTTON)
    find_element_with_time(browser, user_time, ProductPage.PRODUCT_IMG)


def find_element_with_time(browser, user_time, locator):
    try:
        by_selector = By.CSS_SELECTOR
        element = WebDriverWait(browser, user_time).until(EC.visibility_of_element_located((by_selector,
                                                                                            locator)))
        return element

    except TimeoutException:
        print('Объект не найден за указанное время: {}'.format(user_time))

    except NoSuchElementException:
        print('Объект не найден')
