#!/bin/bash
#a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sX OPTIONS $1 -i | grep -i Allow | awk '{$1=""; print substr($0,2)}'
