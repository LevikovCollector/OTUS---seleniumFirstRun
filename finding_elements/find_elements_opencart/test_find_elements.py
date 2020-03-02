from selenium.webdriver.common.keys import Keys

from finding_elements.locators import MainPage, AdminAuthPage, CategoryPage, SearchResultPage, ProductPage


def test_main_page(open_browser):
    '''Проверяем элементы главной страницы'''
    open_browser.get("http://localhost/opencart/")
    open_browser.find_element(*MainPage.ADD_TO_CART_BUTTON)
    open_browser.find_element(*MainPage.MENU_ITEM)
    open_browser.find_element(*MainPage.PRODUCT_CART)
    open_browser.find_element(*MainPage.SEARCH_FIELD)
    open_browser.find_element(*MainPage.SHOPPING_CART_LINK)
    open_browser.find_element(*MainPage.TOP_NAVIGATION)


def test_admin_page(open_browser):
    '''Проверяем элементы страницы авторизации администратора'''
    open_browser.get("http://localhost/opencart/admin/")
    open_browser.find_element(*AdminAuthPage.FORGOT_LINK)
    open_browser.find_element(*AdminAuthPage.HEADER_AUTH_FORM)
    open_browser.find_element(*AdminAuthPage.LOGIN_BUTTON)
    open_browser.find_element(*AdminAuthPage.LOGIN_FIELD)
    open_browser.find_element(*AdminAuthPage.PASSWORD_FIELD)


def test_category_page(open_browser):
    '''Проверяем элементы на страницы с каталогом'''
    open_browser.get("http://localhost/opencart/")
    open_browser.find_element(*MainPage.MENU_ITEM).click()
    open_browser.find_element(*CategoryPage.ADD_PRODUCT_BUTTON)
    open_browser.find_element(*CategoryPage.CONTENT_HEADER)
    open_browser.find_element(*CategoryPage.GRID_VISUAL_TYPE)
    open_browser.find_element(*CategoryPage.LIST_VISUAL_TYPE)
    open_browser.find_element(*CategoryPage.PRODUCT_PREVIEW)
    open_browser.find_element(*CategoryPage.WISH_LIST_BUTTON)


def test_search_result_page(open_browser):
    '''Проверяем элементы на странице с результатами поиска'''
    open_browser.get("http://localhost/opencart/")
    search_field = open_browser.find_element(*MainPage.SEARCH_FIELD)
    search_field.send_keys('iphone')
    search_field.send_keys(Keys.ENTER)

    open_browser.find_element(*SearchResultPage.SEARCH_FIELD)
    open_browser.find_element(*SearchResultPage.ADD_CART_BUTTON)
    open_browser.find_element(*SearchResultPage.CATEGORIES_DROPDOWN)
    open_browser.find_element(*SearchResultPage.SEARCH_RESULT)
    open_browser.find_element(*SearchResultPage.SHOW_DROPDOWN)
    open_browser.find_element(*SearchResultPage.SORT_BY_DROPDOWN)


def test_product_page(open_browser):
    '''Проверяем элементы страницы выбранного продукта'''
    open_browser.get("http://localhost/opencart/")
    open_browser.find_element(*MainPage.PRODUCT_CART).click()

    open_browser.find_element(*ProductPage.WISH_LIST_BUTTON)
    open_browser.find_element(*ProductPage.ADD_PRODUCT_BUTTON)
    open_browser.find_element(*ProductPage.PRODUCT_DESCRIPTION)
    open_browser.find_element(*ProductPage.PRODUCT_IMG)
    open_browser.find_element(*ProductPage.PRODUCT_PRICE)
