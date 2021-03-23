#!/usr/bin/node
module.exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let res = 0;
  for (; i < list.length; i++) {
    if (searchElement === list[i]) {
      res++;
    }
  }
  return res;
};
