from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def test_challenge2(copart):
    copart.find_element_by_css_selector('#input-search').send_keys('exotics')
    copart.find_element_by_css_selector('[ng-click="search()"]').click()
    wait = WebDriverWait(driver=copart, timeout=10)
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                               '#serverSideDataTable_processing[style="display: block;"]')))
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                               '#serverSideDataTable_processing[style="display: none;"]')))
    assert copart.find_elements_by_xpath('//span[@data-uname="lotsearchLotmake"][text()="PORSCHE"]')