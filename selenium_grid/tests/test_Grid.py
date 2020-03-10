from selenium_grid.locators import MainPage, CategoryPage, SearchResultPage, ProductPage
from selenium_grid.page_obj.BaseClass import BasePage



def test_main_page(browser):
    '''Проверяем элементы главной страницы'''
    main_page = BasePage(browser)
    main_page.open_url()
    main_page.verify_element(MainPage.ADD_TO_CART_BUTTON)
    main_page.verify_element(MainPage.MENU_ITEM)
    main_page.verify_element(MainPage.PRODUCT_CART)
    main_page.verify_element(MainPage.SEARCH_FIELD)
    main_page.verify_element(MainPage.SHOPPING_CART_LINK)
    main_page.verify_element(MainPage.TOP_NAVIGATION)


def test_category_page(browser):
    '''Проверяем элементы на страницы с каталогом'''
    category_page = BasePage(browser)
    category_page.open_url()
    category_page.click_element(MainPage.MENU_ITEM)
    category_page.verify_element(CategoryPage.ADD_PRODUCT_BUTTON)
    category_page.verify_element(CategoryPage.CONTENT_HEADER)
    category_page.verify_element(CategoryPage.GRID_VISUAL_TYPE)
    category_page.verify_element(CategoryPage.LIST_VISUAL_TYPE)
    category_page.verify_element(CategoryPage.PRODUCT_PREVIEW)
    category_page.verify_element(CategoryPage.WISH_LIST_BUTTON)


def test_search_result_page(browser):
    '''Проверяем элементы на странице с результатами поиска'''
    search_page = BasePage(browser)
    search_page.open_url()
    search_page.fill_form(MainPage.SEARCH_FIELD, 'MacBook Air', True)
    search_page.verify_element(SearchResultPage.SEARCH_FIELD)
    search_page.verify_element(SearchResultPage.ADD_CART_BUTTON)
    search_page.verify_element(SearchResultPage.CATEGORIES_DROPDOWN)
    search_page.verify_element(SearchResultPage.SEARCH_RESULT)
    search_page.verify_element(SearchResultPage.SHOW_DROPDOWN)
    search_page.verify_element(SearchResultPage.SORT_BY_DROPDOWN)

def test_product_page(browser):
    '''Проверяем элементы страницы выбранного продукта'''
    product_page = BasePage(browser)
    product_page.open_url()
    product_page.click_element(MainPage.PRODUCT_CART)
    product_page.find_element(ProductPage.WISH_LIST_BUTTON)
    product_page.find_element(ProductPage.ADD_PRODUCT_BUTTON)
    product_page.find_element(ProductPage.PRODUCT_DESCRIPTION)
    product_page.find_element(ProductPage.PRODUCT_IMG)
    product_page.find_element(ProductPage.PRODUCT_PRICE)
