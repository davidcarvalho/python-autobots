import pytest


@pytest.fixture
def copart(driver):
    driver.get('https://www.copart.com/')
    return driver
