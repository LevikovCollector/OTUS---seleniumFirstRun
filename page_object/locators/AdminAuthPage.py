from selenium.webdriver.common.by import By


class AdminAuthPage():
    LOGIN_FIELD = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    FORGOT_LINK = (By.CSS_SELECTOR, "span.help-block>a")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "div.text-right>button")
    HEADER_AUTH_FORM = (By.CSS_SELECTOR, "div.panel-heading>h1")
