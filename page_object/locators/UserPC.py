from selenium.webdriver.common.by import By

class UserPersonalCabinet():
    LOGOUT_MENU = (By.XPATH, "//ul/li/a[text()='Logout']")
    CONGRULATIONS_TEXT = (By.XPATH, "//div[@id='content']/p[text()='Congratulations! Your new account has been successfully created!']")
    HEADERS_AFTER_AUTH = (By.CSS_SELECTOR, "#content h2")