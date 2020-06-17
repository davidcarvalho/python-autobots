
def test_challenge1(driver):
    driver.get('https://www.google.com')
    search_textbox = driver.find_element_by_css_selector('input[name=q]')
    search_textbox.send_keys('puppies')
    search_textbox.submit()
    assert 'puppies' in driver.title
