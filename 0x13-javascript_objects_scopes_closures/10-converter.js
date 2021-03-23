#!/usr/bin/node
module.exports.converter = function (base) {
  return function (y) {
    return y.toString(base);
  };
};
