from test_with_db.PO.AdminProductPage import AdminProduct


def test_add_product(browser):
    '''Проверяем добавление нового продукта в каталог'''
    admin_product_page = AdminProduct(browser)
    admin_product_page.open_url('/admin')
    admin_product_page.admin_auth()
    admin_product_page.close_warning_message()
    admin_product_page.open_product_page()
    admin_product_page.product_cart()
    admin_product_page.verify_product_in_table()
    admin_product_page.check_new_product_in_data_base()

def test_edit_product(browser):
    '''Проверяем редактирование продукта'''
    admin_product_page = AdminProduct(browser)
    admin_product_page.add_db_obj('e')
    admin_product_page.open_url('/admin')
    admin_product_page.admin_auth()
    admin_product_page.close_warning_message()
    admin_product_page.open_product_page()
    admin_product_page.edit_product()
    admin_product_page.verify_product_in_table()
    admin_product_page.check_new_product_in_data_base()

def test_delete_product(browser):
    '''Проверяем удаление продукта'''
    admin_product_page = AdminProduct(browser)
    admin_product_page.add_db_obj('d')
    admin_product_page.open_url('/admin')
    admin_product_page.admin_auth()
    admin_product_page.close_warning_message()
    admin_product_page.open_product_page()
    admin_product_page.delete_product()
    admin_product_page.verify_delete_product_in_table()
