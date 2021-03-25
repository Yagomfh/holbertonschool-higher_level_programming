#!/usr/bin/node
const fs = require('fs');
const text1 = fs.readFileSync(process.argv[2], 'utf-8');
const text2 = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFile(process.argv[4], text1 + text2, function (err, result) {
  if (err) console.log('error', err);
});
