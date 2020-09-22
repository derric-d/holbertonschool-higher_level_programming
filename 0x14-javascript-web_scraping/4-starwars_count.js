#!/usr/bin/node
const request = require('request');
const waId = '/18/';
const url = 'https://swapi-api.hbtn.io/api/films';
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    let cnt = 0;
    for (const film of JSON.parse(body).results) {
      for (const ch of film.characters) {
        if (ch.includes(waId)) {
          cnt += 1;
        } else {
          cnt += 0;
        }
      }
    }
    console.log(cnt);
  }
});
