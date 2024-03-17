#!/usr/bin/node

/**
 * This defines a Square.
 * It inherits from Rectangle of 4-rectangle.js
 */

module.exports = class Square extends require('./4-rectangle.js') {
  /**
   * The constructor takes 1 argument "size".
   * The constructor of Rectangle must be called (by using super())
   */
  constructor (size) {
    super(size, size);
  }
};
