#!/usr/bin/node
// script that prints 3 lines with a loop

const lines = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let i = 0;
const len = lines.length;

for (; i < len; i++) {
  console.log(lines[i]);
}
