#!/usr/bin/node
// Prints My number: <first argument converted in integer>

const args = process.argv;
let num = parseInt(args[2]);
let row = 'X';
let i = num;

if (isNaN(num)) {
  console.log('Missing size');
}

for (; i > 1; i--) {
  row += 'X';
}

for (; num > 0; num--) {
  console.log(row);
}
