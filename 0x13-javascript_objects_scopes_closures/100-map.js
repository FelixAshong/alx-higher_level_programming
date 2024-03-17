#!/usr/bin/node

/**
 * Imports an array and computes a new array
 * Imports list from the file 100-data.js
 * New list is created with each value equal
 *    to the value of the initial list,
 *    multipled by the index in the list
 * Both the initial list and the new list are printed
 */

console.log(require('./100-data.js').list);
console.log((require('./100-data.js').list).map((a, b) => a * b));
