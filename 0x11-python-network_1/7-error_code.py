#!/usr/bin/python3
"""
   a Python script that takes in a url:
   and post an email to  the url
   and displays the body of the content of the response
"""

import requests
from sys import argv


def main(url):
    """main function that executes the task"""
    try:
        r = requests.get(url)
        print(r.text)
    except requests.exceptions.HTTPError as err:
        print(f"Error code: {err.errno}")


if __name__ == "__main__":
    main(argv[1])
