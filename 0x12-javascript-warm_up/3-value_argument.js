#!/usr/bin/node
// prints the first argument passed to it

const process = require('process');

const args = process.argv;
let count = 0;

while (args[count] !== undefined) {
  count++;
}

if (count === 3) {
  console.log(args[2]);
}
if (count < 3) {
  console.log('No argument');
}
