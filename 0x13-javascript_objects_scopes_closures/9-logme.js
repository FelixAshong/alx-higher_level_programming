#!/usr/bin/node

/**
 * Prints the number of arguments already printed
 * And the new argument value.
 */

let nArgs = 0;
exports.logMe = function (item) {
  console.log(nArgs + ': ' + item);
  nArgs++;
};
