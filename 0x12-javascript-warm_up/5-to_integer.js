#!/usr/bin/node

const process = require('process');
const args = process.argv

const myVar = parseInt(args[2]);

if (!myVar) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myVar);
}
