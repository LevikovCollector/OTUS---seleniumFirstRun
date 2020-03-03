import os
import random

from faker import Faker
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from page_object.locators import AdminProductPage, AdminProductCart
from page_object.pages_obj.AdminPage import AdminMainPage


class AdminProduct(AdminMainPage):
    def product_cart(self, what_to_do):
        self.product = NewProduct()
        self.product_url = self.driver.current_url
        if what_to_do == 'new':
            self.click_element(AdminProductPage.ADD_NEW_PRODUCT)
        elif what_to_do == 'edit':
            self.click_element(AdminProductPage.EDIT_PRODUCT)

        if self.find_element(AdminProductCart.PRODUCT_FORM):
            self.fill_product_cart()
            self.click_element(AdminProductCart.SAVE_PRODUCT_BUTTON)
            self.open_url(self.product_url)
        else:
            raise NoSuchElementException('Не найден элемент по локатору: ' + AdminProductCart.PRODUCT_FORM)

    def delete_product(self):
        self.product_cart('new')
        if self.check_table_line_by_text():
            self.click_element(AdminProductPage.DELETE_PRODUCT)
            Alert(self.driver).accept()
        else:
            raise WebDriverException('В таблице отсутсвует искомый элемент')

    def verify_delete_product(self):
        assert self.find_element(self.create_xpath(self.product.product_name), time=1) is None

    def create_xpath(self, product_name):
        return (By.XPATH, "//td[contains(text(), '{}')]".format(product_name))

    def verify_delete_product_in_table(self):
        pagination = self.verify_pagination()
        if pagination is not None:
            self.verify_delete_product()
            if self.first_page:
                self.click_element(AdminProductPage.LAST_PAGINATION_PAGE)
                self.verify_delete_product()

        else:
            self.verify_delete_product()

    def product_cart_with_img(self):
        self.product = NewProduct()
        self.product_url = self.driver.current_url
        if self.find_element(AdminProductCart.PRODUCT_FORM):
            self.fill_product_cart()
            self.upload_img_to_cart()
            self.click_element(AdminProductCart.SAVE_PRODUCT_BUTTON)
            self.open_url(self.product_url)
        else:
            raise NoSuchElementException('Не найден элемент по локатору: ' + AdminProductCart.PRODUCT_FORM)

    def check_table_line_by_text(self):
        self.first_page = True
        checkbox = self.find_product_in_table()
        if checkbox is None:
            pagination = self.verify_pagination()
            if pagination is not None:
                self.click_element(AdminProductPage.LAST_PAGINATION_PAGE)
                checkbox = self.find_product_in_table()
                self.click_without_locator(checkbox)

                self.first_page = False
                return True
            else:
                return False
        else:
            self.click_without_locator(checkbox)
            return True

    def find_product_in_table(self):
        all_table_elemnts = self.find_element(AdminProductPage.ALL_TABLE_LINES, many_elements=True)
        for element in all_table_elemnts:
            element_text = self.find_element(AdminProductPage.COLUMN_PRODUCT_NAME, parent_element=element).text
            if element_text == self.product.product_name:
                return self.find_element(AdminProductPage.COLUMN_WITH_CHECKBOX, parent_element=element)

        return None

    def fill_product_cart(self):
        self.fill_form(AdminProductCart.PRODUCT_NAME_FIELD, self.product.product_name)
        self.fill_form(AdminProductCart.PRODUCT_DESCRIPTION_FIELD, self.product.description)
        self.fill_form(AdminProductCart.PRODUCT_META_TAG_FIELD, self.product.tag)

        self.click_element(AdminProductCart.DATA_TAB)
        self.fill_form(AdminProductCart.PRODUCT_PRICE, self.product.product_price)
        self.fill_form(AdminProductCart.PRODUCT_MODEL, self.product.model)

    def upload_img_to_cart(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'img/img1.jpg')
        self.click_element(AdminProductCart.IMG_TAB)
        self.click_element(AdminProductCart.DEFAULT_IMG)
        self.click_element(AdminProductCart.OPEN_IMG_MANAGER)

        self.driver.execute_script("document.getElementById('input-image').setAttribute('type','show')")
        self.fill_form(AdminProductCart.IMG_INPUT, filename)

    def verify_pagination(self):
        return self.find_element(AdminProductPage.PAGINATIONS)

    def verify_product_in_table(self):
        pagination = self.verify_pagination()
        if pagination is not None:
            self.click_element(AdminProductPage.LAST_PAGINATION_PAGE)
            self.verify_product()
        else:
            self.verify_product()

    def verify_product(self):
        '''Функция для поиска в таблице по названию нового продукта'''
        all_table_elemnts = self.find_element(AdminProductPage.ALL_TABLE_LINES, many_elements=True)
        for element in all_table_elemnts:
            element_text = self.find_element(AdminProductPage.COLUMN_PRODUCT_NAME, parent_element=element).text
            if element_text == self.product.product_name:
                assert self.find_element(AdminProductPage.COLUMN_MODEL,
                                         parent_element=element).text == self.product.model
                assert \
                self.find_element(AdminProductPage.COLUMN_PRICE, parent_element=element).text.replace('$', '').replace(
                    ',',
                    '').split(
                    '.')[0] == str(self.product.product_price)


class NewProduct():
    '''Класс для создания нового продукта'''

    def __init__(self):
        fake = Faker('ru_RU')
        self.product_name = '{}{}'.format('Новый товар № ', random.randrange(0, 100))
        self.product_price = random.randrange(10, 10000)
        self.description = fake.text()
        self.tag = 'Test TAG'
        self.model = 'New model'
