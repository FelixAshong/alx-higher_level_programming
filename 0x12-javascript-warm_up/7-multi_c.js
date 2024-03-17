#!/usr/bin/node
if (process.argv.length === 2 || isNaN(Math.floor(Number(process.argv[2])))) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < process.argv[2]; i++) {
  console.log('C is fun');
}
