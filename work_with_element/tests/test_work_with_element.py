import random

from faker import Faker
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait

from work_with_element.locators.AdminAuthPage import AdminAuthPage
from work_with_element.locators.AdminMainPage import AdminMainPage
from work_with_element.locators.AdminProductCart import AdminProductCart
from work_with_element.locators.AdminProductPage import AdminProductPage


def test_add_new_product(open_browser):
    '''Проверка добавления нового продукта'''
    auth_admin(open_browser)
    open_product_page(open_browser)

    product_url = open_browser.current_url

    open_browser.find_element(*AdminProductPage.ADD_NEW_PRODUCT).click()
    assert open_browser.find_element(*AdminProductCart.PRODUCT_FORM).is_displayed()

    product = NewProduct()
    open_browser.find_element(*AdminProductCart.PRODUCT_NAME_FIELD).send_keys(product.product_name)
    open_browser.find_element(*AdminProductCart.PRODUCT_DESCRIPTION_FIELD).send_keys(product.description)
    open_browser.find_element(*AdminProductCart.PRODUCT_META_TAG_FIELD).send_keys(product.tag)

    open_browser.find_element(*AdminProductCart.DATA_TAB).click()
    open_browser.find_element(*AdminProductCart.PRODUCT_PRICE).send_keys(product.product_price)
    open_browser.find_element(*AdminProductCart.PRODUCT_MODEL).send_keys(product.model)

    open_browser.find_element(*AdminProductCart.SAVE_PRODUCT_BUTTON).click()

    open_browser.get(product_url)

    if check_visible_element(open_browser, *AdminProductPage.PAGINATIONS):
        open_browser.find_element(*AdminProductPage.PAGINATIONS).find_element(
            *AdminProductPage.LAST_PAGINATION_PAGE).click()
        chek_product(open_browser, product)
    else:
        chek_product(open_browser, product)
    return product


def test_edit_product(open_browser):
    '''Проверка редактирования продукта'''
    auth_admin(open_browser)
    open_product_page(open_browser)

    open_browser.find_element(*AdminProductPage.EDIT_PRODUCT).click()
    assert open_browser.find_element(*AdminProductCart.PRODUCT_FORM).is_displayed()

    product = NewProduct()
    open_browser.find_element(*AdminProductCart.PRODUCT_NAME_FIELD).clear()
    open_browser.find_element(*AdminProductCart.PRODUCT_DESCRIPTION_FIELD).clear()
    open_browser.find_element(*AdminProductCart.PRODUCT_META_TAG_FIELD).clear()

    open_browser.find_element(*AdminProductCart.PRODUCT_NAME_FIELD).send_keys(product.product_name)
    open_browser.find_element(*AdminProductCart.PRODUCT_DESCRIPTION_FIELD).send_keys(product.description)
    open_browser.find_element(*AdminProductCart.PRODUCT_META_TAG_FIELD).send_keys(product.tag)

    open_browser.find_element(*AdminProductCart.DATA_TAB).click()

    open_browser.find_element(*AdminProductCart.PRODUCT_PRICE).clear()
    open_browser.find_element(*AdminProductCart.PRODUCT_MODEL).clear()

    open_browser.find_element(*AdminProductCart.PRODUCT_PRICE).send_keys(product.product_price)
    open_browser.find_element(*AdminProductCart.PRODUCT_MODEL).send_keys(product.model)

    open_browser.find_element(*AdminProductCart.SAVE_PRODUCT_BUTTON).click()

    if check_visible_element(open_browser, *AdminProductPage.PAGINATIONS):
        open_browser.find_element(*AdminProductPage.PAGINATIONS).find_element(
            *AdminProductPage.LAST_PAGINATION_PAGE).click()
        chek_product(open_browser, product)
    else:
        chek_product(open_browser, product)


def test_delet_product(open_browser):
    '''Удаление добавленного элемента'''

    new_product = test_add_new_product(open_browser)

    all_table_elemnts = open_browser.find_elements(*AdminProductPage.ALL_TABLE_LINES)
    for element in all_table_elemnts:
        element_text = element.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
        if element_text == new_product.product_name:
            element.find_element(By.CSS_SELECTOR, "td:nth-child(1)").click()

    open_browser.find_element(*AdminProductPage.DELETE_PRODUCT).click()
    Alert(open_browser).accept()
    assert status_deleted_product(open_browser, new_product.product_name)


def status_deleted_product(open_browser, product_name):
    try:
        open_browser.find_element(By.XPATH, "//td[contains(text(), '{}')]".format(product_name))
        return False
    except NoSuchElementException:
        return True


def auth_admin(open_browser):
    '''Авторизация в админке opencart'''
    open_browser.find_element(*AdminAuthPage.LOGIN_FIELD).send_keys('admin')
    open_browser.find_element(*AdminAuthPage.PASSWORD_FIELD).send_keys('admin')
    open_browser.find_element(*AdminAuthPage.LOGIN_BUTTON).click()


def open_product_page(open_browser):
    '''Выбор пункта Products из меню'''
    open_browser.find_element(*AdminMainPage.CLOSE_WARNING_MESSAGE).click()
    open_browser.find_element(*AdminMainPage.CATALOG_GROUP).click()
    element = WebDriverWait(open_browser, 10).until(ES.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                      AdminMainPage.PRODUCT_ELEMENT)))
    element.click()


def chek_product(open_browser, new_product):
    '''Функция для поиска в таблице по названию нового продукта'''
    all_table_elemnts = open_browser.find_elements(*AdminProductPage.ALL_TABLE_LINES)
    for element in all_table_elemnts:
        element_text = element.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
        if element_text == new_product.product_name:
            assert element.find_element(By.CSS_SELECTOR, "td:nth-child(4)").text == new_product.model
            assert \
                element.find_element(By.CSS_SELECTOR, "td:nth-child(5)").text.replace('$', '').replace(',', '').split(
                    '.')[
                    0] == str(new_product.product_price)


def check_visible_element(open_browser, by, locator):
    '''Функция в которой проверяется отображение элемента'''
    try:
        return open_browser.find_element(by, locator).is_displayed()
    except NoSuchElementException:
        return False


class NewProduct():
    '''Класс для создания нового продукта'''

    def __init__(self):
        fake = Faker('ru_RU')
        self.product_name = '{}{}'.format('Новый товар № ', random.randrange(0, 100))
        self.product_price = random.randrange(10, 10000)
        self.description = fake.text()
        self.tag = 'Test TAG'
        self.model = 'New model'
