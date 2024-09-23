#!/usr/bin/node

const request = require("request");
const process = require("process");

// Get the first argument
const firstArgument = process.argv[2];
const endPoint = "https://swapi-api.alx-tools.com/api/films";

// Check if the argument is a number using isNaN()
if (isNaN(firstArgument) || firstArgument == 0) {
	process.exit();
}

request(endPoint, function (error, response, body) {
	if (error) {
		console.error("error:", error);
		console.log("statusCode:", response && response.statusCode);
	}

	let rep = JSON.parse(body);
	let film = rep.results[firstArgument - 1];
	let charactersUrls = film.characters;

	let characters = [];

	for (let i = 0; i < charactersUrls.length; i++) {
		request(charactersUrls[i], function (error, response, body) {
			let rep = JSON.parse(body);
			characters.push({
				name: rep.name,
				id: i,
			});
		});
	}

	let ref;

	ref = setInterval(() => {
		if (characters.length == charactersUrls.length) {
			// Sort by id
			characters.sort((a, b) => a.id - b.id);
			for (let character of characters) console.log(character.name);
			clearInterval(ref);
		}
	}, 250);
});
