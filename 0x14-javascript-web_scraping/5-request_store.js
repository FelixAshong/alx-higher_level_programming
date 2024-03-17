#!/usr/bin/node
/* gets the contents of a webpage and stores it in a file.
    - the first argument is the URL to request.
    - the second argument the file path to store the body response.
*/
const request = require('request');
const fs = require('fs');
request(process.argv[2], function (error, response, body) {
  if (error) console.log(error);
  else {
    fs.writeFile(process.argv[3], body, 'utf-8', function (error) {
      if (error) console.log(error);
    });
  }
});
