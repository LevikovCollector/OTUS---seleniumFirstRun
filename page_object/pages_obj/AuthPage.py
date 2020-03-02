from page_object.locators import MainPage, UserPersonalCabinet, AuthPage
from page_object.pages_obj.BaseClass import BasePage


class AuthUser(BasePage):
    def open_auth_form(self):
        self.click_element(MainPage.ACCOUNT_ITEM)
        self.click_element(MainPage.LOGIN_ITEM)
        self.verify_element(AuthPage.AUTH_FORM)

    def fill_auth_form(self):
        self.fill_form(AuthPage.LOGIN_FIELD, 'test1@test1.ru')
        self.fill_form(AuthPage.PASSWORD_FIELD, 'qwe123')

    def click_login(self):
        self.click_element(AuthPage.LOGIN_BUTTON)

    def verify_auth(self):
        self.verify_url('account/account')
        headers = self.find_element(UserPersonalCabinet.HEADERS_AFTER_AUTH, many_elements= True)
        assert len(headers) == 4