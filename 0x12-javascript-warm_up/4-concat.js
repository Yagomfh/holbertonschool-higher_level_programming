#!/usr/bin/node
// prints two arguments passed to it

const args = process.argv;
const res = args[2] + ' is ' + args[3];

console.log(res);
