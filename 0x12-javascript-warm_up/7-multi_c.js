#!/usr/bin/node

const process = require('process');
const args = process.argv;

const num = parseInt(args[2]);

if (!num) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
  console.log('C is fun')
}
}
