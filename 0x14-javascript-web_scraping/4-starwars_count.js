#!/usr/bin/node
// JavaScript - Web scraping

const process = require('process');
const request = require('request');
const args = process.argv;
const url = args[2];
const options = { json: true };
const WedgeAntilles = 'https://swapi-api.hbtn.io/api/people/18/';

request(url, options, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  let count = 0;
  const films = body.results;
  for (const i in films) {
    if (films[i].characters.includes(WedgeAntilles)) {
      count += 1;
    }
  }
  console.log(count);
});
