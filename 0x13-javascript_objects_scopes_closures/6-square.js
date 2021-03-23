#!/usr/bin/node
class Square extends require('./5-square.js') {
  charPrint (c) {
    let myChar;
    if (typeof (c) === 'undefined') {
      myChar = 'X';
    } else {
      myChar = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(myChar.repeat(this.width));
    }
  }
}

module.exports = Square;
