#!/usr/bin/node
// JavaScript - Web scraping

const process = require('process');
const request = require('request');
const args = process.argv;
const url = args[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log('code', response.statusCode);
});
