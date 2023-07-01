#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """

import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as res:
    data = res.read()
print(f"Body response:\n\t- type: {type(data)}\n\t- content: {data}\n\t- utf8 content: {data.decode('utf-8')}")
