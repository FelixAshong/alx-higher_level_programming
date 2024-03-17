#!/usr/bin/node

/**
 * This defines a Square.
 * It inherits from Square of 5-square.js
 */

module.exports = class Square extends require('./5-square.js') {
  /**
   * Creates an instance method called charPrint(c).
   * Prints the rectangle using the character c
   * Uses the character X If c is undefined
   */
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
