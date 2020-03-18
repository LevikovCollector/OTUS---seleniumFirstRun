from selenium.webdriver.common.by import By


class ProductPage():
    WISH_LIST_BUTTON = (By.CSS_SELECTOR, "div.btn-group > button[data-original-title='Add to Wish List']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-4  * >  h2")
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, "div.form-group > #button-cart")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "div.tab-content")
    PRODUCT_IMG = (By.CSS_SELECTOR, "div.col-sm-8 a.thumbnail>img")
