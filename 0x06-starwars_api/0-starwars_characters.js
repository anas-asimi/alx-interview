#!/usr/bin/node

const request = require('request');
const process = require('process');

// Get the first argument
const firstArgument = process.argv[2];
const endPoint = 'https://swapi-api.alx-tools.com/api/films';

// Check if the argument is a number using isNaN()
if (isNaN(firstArgument) || firstArgument === 0) {
  process.exit();
}

request(endPoint, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    console.log('statusCode:', response && response.statusCode);
  }

  const rep = JSON.parse(body);
  const film = rep.results[firstArgument - 1];
  const charactersUrls = film.characters;

  const characters = [];

  for (let i = 0; i < charactersUrls.length; i++) {
    request(charactersUrls[i], function (error, response, body) {
      if (error) {
        console.error('error:', error);
        console.log('statusCode:', response && response.statusCode);
      }
      const rep = JSON.parse(body);
      characters.push({
        name: rep.name,
        id: i
      });
    });
  }

  const ref = setInterval(() => {
    if (characters.length === charactersUrls.length) {
      // Sort by id
      characters.sort((a, b) => a.id - b.id);
      for (const character of characters) console.log(character.name);
      clearInterval(ref);
    }
  }, 250);
});
