import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # code before yield is run Before Each test
    options = webdriver.ChromeOptions()
    # start as maximized windows
    options.add_argument('--start-maximized')
    # disable the infobar at the top of the browser
    options.add_argument('--disable-infobars')
    # disable certain warning messages when chrome launches
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(executable_path='../venv/chromedriver_win32/chromedriver.exe', options=options)
    driver.implicitly_wait(5)
    yield driver
    # code after yield is run After Each test
    driver.quit()
