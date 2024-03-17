#!/usr/bin/node
/* prints the title of a Star Wars movie where the episode number matches a given integer.
    - the first argument is the movie ID.
    - use Star Wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
*/
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) console.log(error);
  else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
