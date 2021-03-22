#!/usr/bin/node
// Prints My number: <first argument converted in integer>

const args = process.argv;
let num = parseInt(args[2]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
}
for (; num > 0; num--) {
  console.log('C is fun');
}
