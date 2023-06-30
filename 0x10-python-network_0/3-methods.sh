#!/bin/bash
#a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sX OPTIONS $1 -i | grep -i Allow | awk '{out=$2; for(i=3;i<=NF;i++){out=out" "$i}; print out}'
