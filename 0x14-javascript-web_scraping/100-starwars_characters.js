#!/usr/bin/node
// JavaScript - Web scraping

const process = require('process');
const request = require('request');
const args = process.argv;
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
const movieId = args[2];
const url = apiUrl + movieId;
const options = { json: true };

request(url, options, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const casting = body.characters;
  for (const i in casting) {
    request(casting[i], options, function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      } else {
        console.log(body.name);
      }
    });
  }
});
