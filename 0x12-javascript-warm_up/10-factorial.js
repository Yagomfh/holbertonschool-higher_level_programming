#!/usr/bin/node
// factorial recursively

const args = process.argv;
const num = parseInt(args[2]);

function factorial (a) {
  if (a === 1) {
    return 1;
  }
  return a * factorial(a - 1);
}

if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
