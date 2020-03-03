from selenium.webdriver.common.by import By


class AdminProductCart():
    PRODUCT_FORM = (By.CSS_SELECTOR, "#content #form-product")
    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, " #form-product #input-name1")
    PRODUCT_DESCRIPTION_FIELD = (By.CSS_SELECTOR, "#form-product div.note-editable.panel-body")
    PRODUCT_META_TAG_FIELD = (By.CSS_SELECTOR, "#form-product #input-meta-title1")
    SAVE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Save']")
    DATA_TAB = (By.CSS_SELECTOR, " #form-product ul.nav.nav-tabs > li:nth-child(2)")
    PRODUCT_MODEL = (By.CSS_SELECTOR, "#form-product #input-model")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#form-product #input-price")
    IMG_TAB = (By.CSS_SELECTOR, "#form-product ul.nav.nav-tabs > li:nth-child(9)")
    IMG_INPUT = (By.CSS_SELECTOR, "input#input-image")
    IMG_MANAGER = (By.CSS_SELECTOR, "#filemanager")
    DEFAULT_IMG = (By.CSS_SELECTOR, "a#thumb-image")
    OPEN_IMG_MANAGER = (By.CSS_SELECTOR,"#button-image")