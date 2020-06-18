from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def test_challenge6(copart):
    wait = WebDriverWait(driver=copart, timeout=10)

    # search for nissan
    search_input = copart.find_element_by_css_selector('#input-search')
    search_input.send_keys('NISSAN')
    copart.find_element_by_css_selector('[ng-click="search()"]').click()

    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                               '#serverSideDataTable_processing[style="display: block;"]')))
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                               '#serverSideDataTable_processing[style="display: none;"]')))

    # search for skyline
    search_input.clear()
    copart.find_element_by_css_selector('#input-search').send_keys('SKYLINE')
    copart.find_element_by_css_selector('[ng-click="search()"]').click()

    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                               '#serverSideDataTable_processing[style="display: block;"]')))
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                               '#serverSideDataTable_processing[style="display: none;"]')))

    try:
        copart.find_element_by_css_selector('tbody span[data-uname="lotsearchLotmodel"]')
        print('model found')
    except NoSuchElementException:
        copart.save_screenshot('../screenshots/tc6_model_not_found.png')