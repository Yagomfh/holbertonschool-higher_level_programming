#!/usr/bin/node
// Prints My number: <first argument converted in integer>

const args = process.argv;

const c = parseInt(args[2]);
const d = parseInt(args[3]);

function add (a, b) {
  return a + b;
}

if (isNaN(c) || isNaN(d)) {
  console.log('NaN');
} else {
  console.log(add(c, d));
}
