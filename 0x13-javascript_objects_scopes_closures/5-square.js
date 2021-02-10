#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle ✅
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
