from faker import Faker

from page_object.locators import MainPage, RegPage, UserPersonalCabinet
from page_object.pages_obj.BaseClass import BasePage


class RegistrationOpenCart(BasePage):
    def fill_registration_form(self):
        new_prof = NewProfile()
        self.fill_form(RegPage.FIRST_NAME_FIELD, new_prof.name)
        self.fill_form(RegPage.LAST_NAME_FIELD, new_prof.last_name)
        self.fill_form(RegPage.TELEPHONE_FIELD, new_prof.telephone)
        self.fill_form(RegPage.EMAIL_FIELD, new_prof.email)
        self.fill_form(RegPage.PASSWORD_FIELD, new_prof.passwd)
        self.fill_form(RegPage.PASSWORD_CONF_FIELD, new_prof.passwd)

    def check_privacy(self):
        self.click_element(RegPage.CHECKBOX_PRIVATE)

    def click_continue_button(self):
        self.click_element(RegPage.CONTINUE_BUTTON)

    def verify_gonrulation_after_registration(self):
        self.verify_element(UserPersonalCabinet.CONGRULATIONS_TEXT)

    def open_registration_form(self):
        self.click_element(MainPage.ACCOUNT_ITEM)
        self.click_element(MainPage.REGISTRATION_ITEM)
        self.verify_element(RegPage.REGISTRATION_FORM)


class NewProfile():
    def __init__(self):
        fake = Faker('Ru_ru')
        self.last_name, other, self.name = fake.name().split(' ')
        self.passwd = 'qwe123'
        self.email = fake.email()
        self.telephone = '123456789'
