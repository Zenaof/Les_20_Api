import requests
import pprint

domain = "https://api.hh.ru/"

url_vacan = f'{domain}vacancies'

# params = {
#     'text': 'C# developer',
#     'page': 1
# }
# result = requests.get(url_vacan, params = params).json()
#
# items = result['items']
#
# first = items[0]
# one_vacancy_url = (first['url'])

params = {
    'text': 'NAME:(Python or Java) AND COMPANY_NAME:(1 OR 2 OR Yandex) AND (Django OR Spring)',
    'page': 1
}


result = requests.get(url_vacan, params = params).json()
pprint.pprint(result)

# print(first['alternate_url'])
# print(first['url'])




# print(result.status_code)
# pprint.pprint(result.json())