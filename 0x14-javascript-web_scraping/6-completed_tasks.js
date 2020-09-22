#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const newDict = {};
  const bod = JSON.parse(body);
  for (let i = 0; i < bod.length; i++) {
    const uid = bod[i].userId;
    if (bod[i].completed) {
      if (uid in newDict) {
        newDict[uid] += 1;
      } else {
        newDict[uid] = 1;
      }
    }
  }
  console.log(newDict);
});
