#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = 'X';
    let i;
    for (i = this.width; i > 1; i--) {
      row += 'X';
    }
    for (i = this.height; i > 0; i--) {
      console.log(row);
    }
  }
};
