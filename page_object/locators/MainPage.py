from selenium.webdriver.common.by import By


class MainPage():
    SEARCH_FIELD = (By.CSS_SELECTOR, "#search > input[name='search']")
    TOP_NAVIGATION = (By.CSS_SELECTOR, "ul[class='nav navbar-nav']>li")
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, "ul[class='list-inline']>li:nth-child(4)>a")
    PRODUCT_CART = (By.CSS_SELECTOR, "div[class='product-thumb transition']>div[class='image']>a")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "div.product-thumb.transition>div.button-group>button:first-child")
    MENU_ITEM = (By.CSS_SELECTOR, "#menu  li:nth-child(6)")
    BASKET_BUTTON = (By.CSS_SELECTOR, "#cart")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#cart ul p")
    BASKET_WITH_ITEM = (By.CSS_SELECTOR, "#cart table.table-striped")
    DELETE_ITEM_IN_BASKET = (By.CSS_SELECTOR, "#cart td.text-center>button")
    ACCOUNT_ITEM = (By.CSS_SELECTOR, "ul.list-inline  li:nth-child(2)")
    REGISTRATION_ITEM = (By.XPATH, "//ul/li/a[text()= 'Register']")
    LOGIN_ITEM = (By.XPATH, "//ul/li/a[text()= 'Login']")