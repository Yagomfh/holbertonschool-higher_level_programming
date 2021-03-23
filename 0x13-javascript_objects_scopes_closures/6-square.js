#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let row = 'X';
    let i;
    if (c !== undefined) {
      row = c;
    }
    for (i = this.width; i > 1; i--) {
      if (c !== undefined) {
        row += c;
      } else {
        row += 'X';
      }
    }
    for (i = this.height; i > 0; i--) {
      console.log(row);
    }
  }
};
