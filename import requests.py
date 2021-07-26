import requests


ses = requests.session()
response = ses.get('https://www.zonaprop.com.ar/rp-api/user/session')

print(response)