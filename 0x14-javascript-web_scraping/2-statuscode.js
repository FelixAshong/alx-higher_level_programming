#!/usr/bin/node
/* displays the status code of a GET request.
    - the first argument is the URL to request (GET).
    - output format: 'code: <status code>'.
*/
const request = require('request');
request(process.argv[2], function (error, response) {
  if (error) console.log(error);
  else console.log('code: ' + response.statusCode);
});
