const Square = require('./5-square');

Square.prototype.charPrint = function (c) {
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
};

module.exports = Square;
