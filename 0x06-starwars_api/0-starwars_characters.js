#!/usr/bin/node

const request = require('request');

function sendRequest (characterList, index) {
  if (characterList.length === index) {
    return;
  }

  request(characterList[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const name = JSON.parse(body).name;
      console.log(name);
      sendRequest(characterList, index + 1);
    }
  });
}

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    sendRequest(characters, 0);
  }
});
