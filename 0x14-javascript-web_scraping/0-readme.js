#!/usr/bin/node
/* reads and prints the content of a file.
    - the first argument is the file path.
    - the content of the file is read in utf-8.
    - if an error occurred during the reading, prints the error object.
*/
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', function (error, data) {
  if (error) console.log(error);
  else console.log(data);
});
