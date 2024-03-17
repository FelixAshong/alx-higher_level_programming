#!/usr/bin/node

/**
 * Returns the number of occurrences in a list
 */

exports.nbOccurences = function (list, searchElement) {
  return list.filter(item => item === searchElement).length;
};
