#!/usr/bin/node
// JavaScript - Web scraping

const fs = require('fs');
const process = require('process');
const args = process.argv;
const file = args[2];
const content = args[3];

fs.writeFile(file, content, 'utf-8', err => {
  if (err) {
    console.error(err);
    return;
  }
});
