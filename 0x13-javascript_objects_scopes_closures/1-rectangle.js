#!/usr/bin/node

/**
 * This defines a Rectangle.
 */

module.exports = class Rectangle {
  /**
   * The constructor takes 2 arguments w and h.
   * Instance attribute width with the value of w
   * Instance attribute height with the value of h
   */
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
};
