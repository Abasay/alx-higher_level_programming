#!/usr/bin/node

const process = require('process');
const args = process.argv;
const request = require('request');
const url = args[2];
const fs = require('fs');

request(url).pipe(fs.createWriteStream(args[3]));
