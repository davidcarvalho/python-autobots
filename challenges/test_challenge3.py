

def test_challenge3(copart):
    list_cars = copart.find_elements_by_css_selector('[ng-repeat*="popularSearch"] > a')
    for car in list_cars:
        print(f'{car.text} - {car.get_attribute("href")}')