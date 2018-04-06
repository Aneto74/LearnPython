import requests

res = requests.get('http://aneto.ru/')
res2 = requests.get('http://aneto.ru/3498832940234')

print(res.status_code)
print(res2.status_code)
