#!/usr/bin/node
// prints the first argument passed to it

const args = process.argv;

if (args[2] !== undefined) {
  console.log(args[2]);
} else {
  console.log('No argument');
}
