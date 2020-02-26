from selenium.webdriver.common.by import By


class AdminMainPageLocators():
    CLOSE_WARNING_MESSAGE = (By.CSS_SELECTOR, "#modal-security  button.close")
    CATALOG_GROUP = (By.CSS_SELECTOR, "#menu-catalog  a")
    PRODUCT_ELEMENT = (By.CSS_SELECTOR,"#menu-catalog> #collapse1 > li:nth-child(2)")
