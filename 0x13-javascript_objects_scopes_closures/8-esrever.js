#!/usr/bin/node
module.exports.esrever = function (list) {
  const reversed = [];
  let i;
  for (i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};
