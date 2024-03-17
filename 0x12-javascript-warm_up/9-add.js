#!/usr/bin/node
function add (a, b) {
  return a + b;
}

console.log(add(Math.floor(Number(process.argv[2])), Math.floor(Number(process.argv[3]))));
