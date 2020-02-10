import pytest
from selenium import webdriver


@pytest.fixture
def open_browser(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver
