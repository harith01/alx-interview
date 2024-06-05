#!/usr/bin/node

const request = require('request')
const process = require('process')

let url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, (error, response, body) => {
  if (error) throw new Error(error);
  let characters = JSON.parse(body).characters;
  characters.map((character) => {
    request(character, (error, response, body) => {
      if (error) throw new Error(error);
      console.log(JSON.parse(body).name)
    })
  })
  });
