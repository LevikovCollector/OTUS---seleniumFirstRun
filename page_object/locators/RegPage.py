from selenium.webdriver.common.by import By

class RegPage():
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "input[name='firstname']")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "input[name='lastname']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='email']")
    TELEPHONE_FIELD = (By.CSS_SELECTOR, "input[name='telephone']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='password']")
    PASSWORD_CONF_FIELD = (By.CSS_SELECTOR, "input[name='confirm']")
    CHECKBOX_PRIVATE = (By.CSS_SELECTOR, "input[name='agree']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[value='Continue']")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "form.form-horizontal")





