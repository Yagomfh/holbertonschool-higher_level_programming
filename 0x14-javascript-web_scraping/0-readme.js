#!/usr/bin/node
// JavaScript - Web scraping

const fs = require('fs');
const process = require('process');
const args = process.argv;
const file = args[2];

fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
