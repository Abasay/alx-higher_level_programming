#!/usr/bin/node

const process = require('process');
const args = process.argv;

let max = 0;
let num = 0;

for (let i = 2; i < args.length; i++) {
  num = parseInt(args[i]);
  if (num > max) {
    max = num
