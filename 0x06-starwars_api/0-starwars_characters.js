#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

const filmUrl = 'https://swapi-api.alx-tools.com/api/films/' + args[0];

request(filmUrl, async function (error, response, body) {
  if (!error) {
    const json = JSON.parse(body);
    const charEndpts = json.characters;
    for (const charEndpt of charEndpts) {
      await new Promise(function (resolve, reject) {
        request(charEndpt, function (error, response, body) {
          if (!error) {
            console.log(JSON.parse(body).name);
            resolve();
          }
        });
      });
    }
  }
});
