#Basic Autentication
#Request Module

import requests
from requests.auth import HTTPBasicAuth
#from base64 import b64encode

url = "https://postman-echo.com/basic-auth"
username = "postman"
password = "password"

authObject = HTTPBasicAuth(username, password)

'''
token = (b64encode(( f'{username} : {password}')
                   .encode("utf-8"))).decode()
'''

r = requests.get(url, auth = authObject)
'''
headers = {
    "Authorization": "Basic "+ token
}
r = requests.get(url, headers = headers)
'''

print(r)
