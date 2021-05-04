#!/usr/bin/node
// JavaScript - Web scraping

const process = require('process');
const request = require('request');
const fs = require('fs');
const args = process.argv;
const url = args[2];
const file = args[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  fs.writeFile(file, body, 'utf-8', err => {
    if (err) {
      console.error(err);
    }
  });
});
