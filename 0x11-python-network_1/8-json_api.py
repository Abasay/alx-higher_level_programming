#!/usr/bin/python3
"""
   a Python script that takes in a url:
   and post a leter to  the url as a search param
   and displays the body of the content of the response
"""

import json
import requests
from sys import argv


def main(letter=""):
    """main function that executes the task"""
    try:
        params = {'q': letter}
        r = requests.post('http://0.0.0.0:5000/search_user', data=params)
        result = eval(r.text)
        try:
            print(f"{[result['id']]} {result['name']}")
        except KeyError as e:
            print("Not a result")
    except requests.exceptions.HTTPError as err:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(argv) >= 2:
        main(letter=argv[1])
    else:
        main()
