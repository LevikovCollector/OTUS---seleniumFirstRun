from page_object.locators import MainPage
from page_object.pages_obj.BaseClass import BasePage


class MainOpenCartPage(BasePage):
    def add_product_to_basket(self):
        self.click_element(MainPage.ADD_TO_CART_BUTTON)

    def verify_empety_basket(self):
        self.verify_element(MainPage.EMPTY_BASKET_MESSAGE)

    def verify_basket_with_items(self):
        self.verify_element(MainPage.BASKET_WITH_ITEM)

    def delete_item_from_basket(self):
        self.add_product_to_basket()
        self.open_basket()
        self.click_element(MainPage.DELETE_ITEM_IN_BASKET)

    def open_basket(self):
        self.click_element(MainPage.BASKET_BUTTON)
