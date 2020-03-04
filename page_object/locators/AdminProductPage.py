from selenium.webdriver.common.by import By


class AdminProductPage():
    ADD_NEW_PRODUCT = (By.CSS_SELECTOR, "div.pull-right a[data-original-title='Add New']")
    DELETE_PRODUCT = (By.CSS_SELECTOR, "div.pull-right button[data-original-title='Delete']")
    EDIT_PRODUCT = (By.CSS_SELECTOR, "div.table-responsive tbody >tr:nth-child(1)>td:last-child>a")
    ALL_TABLE_LINES = (By.CSS_SELECTOR, "div.table-responsive tbody >tr")
    PAGINATIONS = (By.CSS_SELECTOR, "ul.pagination")
    LAST_PAGINATION_PAGE = (By.CSS_SELECTOR, "ul.pagination>li:last-child>a")
    COLUMN_PRODUCT_NAME = (By.CSS_SELECTOR, "td:nth-child(3)")
    COLUMN_MODEL = (By.CSS_SELECTOR, "td:nth-child(4)")
    COLUMN_PRICE = (By.CSS_SELECTOR, "td:nth-child(5)")
    COLUMN_WITH_CHECKBOX = (By.CSS_SELECTOR, "td:nth-child(1)")


