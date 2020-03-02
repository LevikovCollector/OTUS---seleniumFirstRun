from selenium.webdriver.common.by import By


class CategoryPage():
    CONTENT_HEADER = (By.CSS_SELECTOR, "#content h2")
    PRODUCT_PREVIEW = (By.CSS_SELECTOR, "#content div.product-thumb")
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, "div.product-thumb div.button-group>button:first-child")
    WISH_LIST_BUTTON = (
    By.CSS_SELECTOR, "div.product-thumb div.button-group>button[data-original-title='Add to Wish List']")
    LIST_VISUAL_TYPE = (By.CSS_SELECTOR, "#list-view")
    GRID_VISUAL_TYPE = (By.CSS_SELECTOR, "#grid-view")
