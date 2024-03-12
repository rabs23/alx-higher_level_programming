#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let v = '';
      for (let j = 0; j < this.width; j++) {
        v += c;
      }
      console.log(v);
    }
  }
}

module.exports = Square;
