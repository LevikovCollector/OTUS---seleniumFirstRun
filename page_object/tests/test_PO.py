from page_object.locators import MainPage, AdminAuthPage, CategoryPage, SearchResultPage, ProductPage, \
    AdminMainPageLocators
from page_object.pages_obj.AdminProductPage import AdminProduct
from page_object.pages_obj.AuthPage import AuthUser
from page_object.pages_obj.BaseClass import BasePage
from page_object.pages_obj.MainPage import MainOpenCartPage
from page_object.pages_obj.RegisterPage import RegistrationOpenCart
from page_object.pages_obj.UserCabinet import UserPersonalCabinetOpenCart


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


def test_admin_page(browser):
    '''Проверяем элементы страницы авторизации администратора'''
    adm_page = BasePage(browser)
    adm_page.open_url('/admin')
    adm_page.verify_element(AdminAuthPage.FORGOT_LINK)
    adm_page.verify_element(AdminAuthPage.HEADER_AUTH_FORM)
    adm_page.verify_element(AdminAuthPage.LOGIN_BUTTON)
    adm_page.verify_element(AdminAuthPage.LOGIN_FIELD)
    adm_page.verify_element(AdminAuthPage.PASSWORD_FIELD)


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


def test_add_product(browser):
    '''Проверяем добавление нового продукта в каталог'''
    admin_product_page = AdminProduct(browser)
    admin_product_page.open_url('/admin')
    admin_product_page.admin_auth()
    admin_product_page.close_warning_message()
    admin_product_page.click_element(AdminMainPageLocators.CATALOG_GROUP)
    admin_product_page.click_element(AdminMainPageLocators.PRODUCT_ELEMENT)
    admin_product_page.product_cart('new')
    admin_product_page.verify_product_in_table()


def test_edit_product(browser):
    '''Проверяем редактирование продукта'''
    admin_product_page = AdminProduct(browser)
    admin_product_page.open_url('/admin')
    admin_product_page.admin_auth()
    admin_product_page.close_warning_message()
    admin_product_page.click_element(AdminMainPageLocators.CATALOG_GROUP)
    admin_product_page.click_element(AdminMainPageLocators.PRODUCT_ELEMENT)
    admin_product_page.product_cart('edit')
    admin_product_page.verify_product_in_table()


def test_delete_product(browser):
    '''Проверяем удаление продукта'''
    admin_product_page = AdminProduct(browser)
    admin_product_page.open_url('/admin')
    admin_product_page.admin_auth()
    admin_product_page.close_warning_message()
    admin_product_page.click_element(AdminMainPageLocators.CATALOG_GROUP)
    admin_product_page.click_element(AdminMainPageLocators.PRODUCT_ELEMENT)
    admin_product_page.delete_product()
    admin_product_page.verify_delete_product_in_table()


def test_empty_message_in_basket(browser):
    '''Проверяем сообщение в пустой корзине'''
    main_page = MainOpenCartPage(browser)
    main_page.open_url()
    main_page.open_basket()
    main_page.verify_empety_basket()


def test_delete_item_from_basket(browser):
    '''Проверяем удаление элемента из корзины'''
    main_page = MainOpenCartPage(browser)
    main_page.open_url()
    main_page.delete_item_from_basket()
    main_page.open_basket()
    main_page.verify_empety_basket()


def test_add_product_to_basket(browser):
    '''Проверяем добавление элемента в корзину'''
    main_page = MainOpenCartPage(browser)
    main_page.open_url()
    main_page.add_product_to_basket()
    main_page.open_basket()
    main_page.verify_basket_with_items()


def test_registration(browser):
    '''Проверяем регистрацию нового пользователя'''
    reg_page = RegistrationOpenCart(browser)
    reg_page.open_url()
    reg_page.open_registration_form()
    reg_page.fill_registration_form()
    reg_page.check_privacy()
    reg_page.click_continue_button()
    reg_page.verify_gonrulation_after_registration()

    user_cabinet = UserPersonalCabinetOpenCart(browser)
    user_cabinet.logout()
    user_cabinet.verify_logout()


def test_auth_user(browser):
    '''Проверяем авторизацию нового пользователя'''
    auth_page = AuthUser(browser)
    auth_page.open_url()
    auth_page.open_auth_form()
    auth_page.fill_auth_form()
    auth_page.click_login()
    auth_page.verify_auth()

    user_cabinet = UserPersonalCabinetOpenCart(browser)
    user_cabinet.logout()
    user_cabinet.verify_logout()
