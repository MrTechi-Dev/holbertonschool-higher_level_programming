#!/usr/bin/node
// Class rectangle ✅ Check if w and h are numbers greater than 0
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w !== 0 && h !== 0) && (w > 0 && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print (width, height) {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate (width, height) {
    [this.width, this.height] = [this.height, this.width];
  }

  double (width, height) {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
}; // end of class
