#!/usr/bin/node

const request = require('request')
const process = require('process')

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

if (process.argv.length > 2) {
  request(url, (error, _, body) => {
    if (error) throw new Error(error);
    const characters = JSON.parse(body).characters;
    const names = characters.map(character => new Promise((resolve, reject) => {
      request(character, (error, _, body) => {
        if (error) throw new Error(error);
	resolve(JSON.parse(body).name);
      })
    }))
    Promise.all(names)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  })
}
