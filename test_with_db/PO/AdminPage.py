from test_with_db.locators import AdminMainPageLocators
from test_with_db.PO.AdminAuthPage import AdminAuth
from test_with_db.PO.BaseClass import BasePage


class AdminMainPage(AdminAuth, BasePage):
    def close_warning_message(self):
        self.click_element(AdminMainPageLocators.CLOSE_WARNING_MESSAGE)
    def open_product_page(self):
        self.click_element(AdminMainPageLocators.CATALOG_GROUP)
        self.click_element(AdminMainPageLocators.PRODUCT_ELEMENT)