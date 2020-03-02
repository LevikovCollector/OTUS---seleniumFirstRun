from selenium.webdriver.common.by import By


class SearchResultPage():
    SEARCH_FIELD = (By.CSS_SELECTOR, "input#input-search")
    CATEGORIES_DROPDOWN = (By.CSS_SELECTOR, "select.form-control[name='category_id']")
    SEARCH_RESULT = (By.CSS_SELECTOR, "div.product-thumb")
    ADD_CART_BUTTON = (By.CSS_SELECTOR, "div.button-group>button:first-child")
    SORT_BY_DROPDOWN = (By.CSS_SELECTOR, "#input-sort")
    SHOW_DROPDOWN = (By.CSS_SELECTOR, "#input-limit")
