#!/usr/bin/node

const process = require('process');
const args = process.argv;
const request = require('request');

requests.get(args[2]).
    on('response', function (response) {
	console.log("code: " + response.statusCode)
    })
