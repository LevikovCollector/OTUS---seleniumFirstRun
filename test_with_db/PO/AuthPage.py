from test_with_db.locators import MainPage, AdminAuthPage
from test_with_db.PO.BaseClass import BasePage


class AuthUser(BasePage):
    def open_auth_form(self):
        self.click_element(MainPage.ACCOUNT_ITEM)
        self.click_element(MainPage.LOGIN_ITEM)
        self.verify_element(AdminAuthPage.HEADER_AUTH_FORM)

    def fill_auth_form(self):
        self.fill_form(AdminAuthPage.LOGIN_FIELD, 'test1@test1.ru')
        self.fill_form(AdminAuthPage.PASSWORD_FIELD, 'qwe123')

    def click_login(self):
        self.click_element(AdminAuthPage.LOGIN_BUTTON)