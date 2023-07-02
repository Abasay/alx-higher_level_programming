#!/usr/bin/python3
"""a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)"""

import urllib.parse
import sys
import urllib.request

email = {'email' : sys.argv[2]}
data = urllib.parse.urlencode(email)
data = data.encode('ascii')
req = urllib.request.Request(sys.argv[1], data)
with urllib.request.urlopen(req) as res:
    the_page = res.read().decode('utf-8')
print(the_page)
