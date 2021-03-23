#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
let idx = 0;
const newList = list.map(x => x * idx++);
console.log(newList);
