from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_challenge5(copart):
    copart.find_element_by_css_selector('#input-search').send_keys('PORSCHE')
    copart.find_element_by_css_selector('[ng-click="search()"').click()

    wait = WebDriverWait(driver=copart, timeout=10)
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                               '#serverSideDataTable_processing[style="display: block;"]')))
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                               '#serverSideDataTable_processing[style="display: none;"]')))

    copart.find_element_by_css_selector('select[name="serverSideDataTable_length"]')
    Select(copart.find_element_by_css_selector('select[name="serverSideDataTable_length"]')).select_by_value('100')
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                               '#serverSideDataTable_processing[style="display: block;"]')))
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                               '#serverSideDataTable_processing[style="display: none;"]')))
    dict_count = {}
    for model in copart.find_elements_by_css_selector('tbody span[data-uname="lotsearchLotmodel"]'):
        if model.text not in dict_count:
            dict_count[model.text] = 1
        else:
            dict_count[model.text] = dict_count.get(model.text) + 1
    print('\n')
    for item in dict_count:
        print(f'x{dict_count.get(item)} {item}')


def test_challenge5_2(copart):
    copart.find_element_by_css_selector('#input-search').send_keys('PORSCHE')
    copart.find_element_by_css_selector('[ng-click="search()"').click()

    wait = WebDriverWait(driver=copart, timeout=10)
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                               '#serverSideDataTable_processing[style="display: block;"]')))
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                               '#serverSideDataTable_processing[style="display: none;"]')))

    copart.find_element_by_css_selector('select[name="serverSideDataTable_length"]')
    Select(copart.find_element_by_css_selector('select[name="serverSideDataTable_length"]')).select_by_value('100')
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                               '#serverSideDataTable_processing[style="display: block;"]')))
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                               '#serverSideDataTable_processing[style="display: none;"]')))
    dict_count = {}
    # damages
    for damage in copart.find_elements_by_css_selector('tbody span[data-uname="lotsearchLotdamagedescription"]'):
        if damage.text in ['REAR END', 'FRONT END', 'MINOR DENT/SCRATCHES', 'UNDERCARRIAGE']:
            if damage.text not in dict_count:
                dict_count[damage.text] = 1
            else:
                dict_count[damage.text] = dict_count.get(damage.text) + 1
        else:
            if 'MISC' not in dict_count:
                dict_count['MISC'] = 1
            else:
                dict_count['MISC'] = dict_count.get('MISC') + 1
    print('\n')
    print(dict_count)
