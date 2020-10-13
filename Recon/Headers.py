#!/usr/bin/python

import requests

myheaders = {'User-Agent': 'Windows 10'}
r = requests.get('http://example.com', headers=myheaders)

print(r.text)