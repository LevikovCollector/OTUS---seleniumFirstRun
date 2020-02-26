from page_object.locators import UserPersonalCabinet, MainPage
from page_object.pages_obj.BaseClass import BasePage


class UserPersonalCabinetOpenCart(BasePage):

    def logout(self):
        self.click_element(MainPage.ACCOUNT_ITEM)
        self.click_element(UserPersonalCabinet.LOGOUT_MENU)

    def verify_logout(self):
        self.verify_url('account/logout')
