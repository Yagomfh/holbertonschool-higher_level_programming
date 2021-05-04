#!/usr/bin/node
// JavaScript - Web scraping

const process = require('process');
const request = require('request');
const args = process.argv;
const url = args[2];
const options = { json: true };

request(url, options, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const res = {};
  const tasks = body;
  for (const i in tasks) {
    if (tasks[i].completed) {
      const user = tasks[i].userId in res;
      if (user) {
        res[tasks[i].userId] += 1;
      } else {
        res[tasks[i].userId] = 1;
      }
    }
  }
  console.log(res);
});
