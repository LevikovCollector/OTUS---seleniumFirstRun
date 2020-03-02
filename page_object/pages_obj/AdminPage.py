from page_object.locators import AdminMainPageLocators
from page_object.pages_obj.AdminAuthPage import AdminAuth
from page_object.pages_obj.BaseClass import BasePage


class AdminMainPage(AdminAuth, BasePage):
    def close_warning_message(self):
        self.click_element(AdminMainPageLocators.CLOSE_WARNING_MESSAGE)
