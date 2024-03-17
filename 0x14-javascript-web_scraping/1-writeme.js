#!/usr/bin/node
/* writes a string to a file.
    - the first argument is the file path.
    - the second argument is the string to write.
    - the content of the file is write in utf-8.
    - if an error occurred during the writing, prints the error object.
*/
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (error) {
  if (error) console.log(error);
});
