import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def browser(request):
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox(firefox_binary='/home/vladimir/firefox/firefox',
    #                            executable_path='/usr/local/bin/geckodriver')
    request.addfinalizer(driver.quit)
    return driver
