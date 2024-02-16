import requests

url = 'https://api.github.com/search/repositories?q=tetris+language:assembly&sort=stars&other=desc'
token = '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'
#
# result = requests.get(url, auth=('Zenaof', token))
#
# headers = {
#     'Autorization': f"tocenP{token}"
# }
#
# result = requests.get(url, headers=headers)

session = requests.session()
session,auth = ('zenaof', token)
# result = session.get(url)

result = session.get(url)
pprint.pprint(result.json())