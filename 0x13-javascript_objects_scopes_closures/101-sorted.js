#!/usr/bin/node

/**
 * Imports a dictionary of occurrences by user id
 * Computes a dictionary of user ids by occurrence.
 */

const dict = require('./101-data.js').dict;
const newDict = {};
for (const key in dict) {
/**
 * In the new dictionary:
 * A key is a number of occurrences
 * A value is the list of user ids
 */
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [key];
  } else {
    newDict[dict[key]].push(key);
  }
}
console.log(newDict);
