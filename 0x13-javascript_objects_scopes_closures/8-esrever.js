#!/usr/bin/node

/**
 * Returns the reversed version of a list
 */

exports.esrever = function (list) {
  const rev = [];
  for (let i = 0; i < list.length; i++) {
    rev[list.length - i - 1] = list[i];
  }
  return rev;
};
