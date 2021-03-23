#!/usr/bin/node
const Rectangle = require('./3-rectangle');

Rectangle.prototype.rotate = function () {
  const tmp = this.width;
  this.width = this.height;
  this.height = tmp;
};

Rectangle.prototype.double = function () {
  this.width *= 2;
  this.height *= 2;
};

module.exports = Rectangle;
