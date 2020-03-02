from selenium.webdriver.common.by import By

class AuthPage():
    LOGIN_FIELD = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value='Login']")
    AUTH_FORM = (By.CSS_SELECTOR, "#content form")