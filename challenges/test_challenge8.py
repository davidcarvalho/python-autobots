import requests


def test_challenge8(driver):
    url = "https://www.copart.com/public/lots/search"
    driver.get(url)
    cookies = ''

    for cookie in driver.get_cookies():
        cookies += cookie["name"]+'='+cookie["value"]+';'
    driver.quit()
    headers = {
        'Cookie': cookies
    }

    cars_i_like = ['toyota corolla', 'toyota elantra', 'toyota acura', 'dodge charger', 'PORSCHE PANAMERA',
                   'PORSCHE CAYENNE', 'HONDA PRIUS', 'HONDA ACCORD', 'Nissan maxima', 'nissan rogue']

    for car in cars_i_like:
        payload = {'query': car}
        response = requests.post(url, headers=headers, data=payload)

        # print(f'\n\n\n{payload}')
        print(f'\n\n\n{response.status_code}')
        print(f'\n\n\n{response.text}')
