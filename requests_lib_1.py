#DIGEST Autentication
#Request Module

import requests
from requests.auth import HTTPDigestAuth

url = "https://postman-echo.com/digest-auth"
username = "postman"
password = "password"

auth = HTTPDigestAuth(username, password)

r = requests.get(url, auth=auth)
print(r.status_code)