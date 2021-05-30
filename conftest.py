import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    # code before yield is run Before Each test
    options = webdriver.ChromeOptions()
    # start as maximized windows
    options.add_argument('--start-maximized')
    # disable the infobar at the top of the browser
    options.add_argument('--disable-infobars')
    # # disable certain warning messages when chrome launches
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(5)
    os.environ['WDM_LOG_LEVEL'] = '0'
    yield driver
    # code after yield is run After Each test
    driver.quit()
