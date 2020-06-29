from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def test_challenge7(copart, driver):
    wait = WebDriverWait(driver=copart, timeout=10)

    list_cars = []
    for car in copart.find_elements_by_css_selector('[ng-repeat*="popularSearch"]>a'):
        list_cars.append([car.text, car.get_attribute('href')])

    for i in range(len(list_cars)):
        driver.get(list_cars[i][1])
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                                   '#serverSideDataTable_processing[style="display: block;"]')))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                                   '#serverSideDataTable_processing[style="display: none;"]')))
        assert list_cars[i][0].replace(' ', '-').lower() \
               in copart.find_element_by_css_selector('h1[data-uname="searchResultsHeader"]').text
