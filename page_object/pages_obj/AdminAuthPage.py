from page_object.locators import AdminAuthPage
from page_object.pages_obj.BaseClass import BasePage


class AdminAuth(BasePage):
    def admin_auth(self):
        self.fill_form(AdminAuthPage.LOGIN_FIELD, 'admin')
        self.fill_form(AdminAuthPage.PASSWORD_FIELD, 'admin')
        self.click_element(AdminAuthPage.LOGIN_BUTTON)
