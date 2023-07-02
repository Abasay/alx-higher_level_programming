#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
"""

import urllib.request
import sys

req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as res:
    data = res.getheader('X-Request-Id')
print(data)
