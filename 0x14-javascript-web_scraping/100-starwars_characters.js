#!/usr/bin/node
/* prints all characters of a Star Wars movie.
    - the first argument is the Movie ID.
    - displays one character name by line.
*/
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) console.log(error);
  else {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (error, response, body) {
        if (error) console.log(error);
        else console.log(JSON.parse(body).name);
      });
    });
  }
});
