from selenium.webdriver.common.by import By


class AdminProductPage():
    ADD_NEW_PRODUCT = (By.CSS_SELECTOR, "div.pull-right a[data-original-title='Add New']")
    DELETE_PRODUCT = (By.CSS_SELECTOR, "div.pull-right button[data-original-title='Delete']")
    EDIT_PRODUCT = (By.CSS_SELECTOR, "div.table-responsive tbody >tr:nth-child(3)>td:last-child>a")
    ALL_TABLE_LINES = (By.CSS_SELECTOR, "div.table-responsive tbody >tr")
    PAGINATIONS = (By.CSS_SELECTOR, "ul.pagination")
    LAST_PAGINATION_PAGE = (By.CSS_SELECTOR, "li:last-child>a")
