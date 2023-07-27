#!/usr/bin/node

const fs = require('fs');
const process = require('process');
const args = process.argv;

fs.writeFile(args[2], args[3], encoding='utf-8', (err) => {
    if (err) {
	console.log(err);
    }
})
