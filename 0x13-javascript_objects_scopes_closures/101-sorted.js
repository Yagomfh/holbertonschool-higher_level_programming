#!/usr/bin/node
const dict = require('./101-data').dict;
let key;
const sorted = {};
for (key in dict) {
  if (sorted[dict[key]] === undefined) {
    sorted[dict[key]] = [];
  }
  sorted[dict[key]].push(key);
}
console.log(sorted);
