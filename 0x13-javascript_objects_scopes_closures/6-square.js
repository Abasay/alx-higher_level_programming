#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    let letter = c;
    if (!c) {
      letter = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(letter.repeat(this.width));
    }
  }
}
