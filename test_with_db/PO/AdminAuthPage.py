from test_with_db.locators import AdminAuthPage
from test_with_db.PO.BaseClass import BasePage


class AdminAuth(BasePage):
    def admin_auth(self):
        self.fill_form(AdminAuthPage.LOGIN_FIELD, 'admin')
        self.fill_form(AdminAuthPage.PASSWORD_FIELD, 'admin')
        self.click_element(AdminAuthPage.LOGIN_BUTTON)
