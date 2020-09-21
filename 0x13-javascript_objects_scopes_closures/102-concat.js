#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], (err, content) => {
  if (err) throw err;

  let newF = content.toString();

  fs.readFile(process.argv[3], (err, content) => {
    if (err) throw err;

    newF += content.toString();
    fs.writeFile(process.argv[4], newF, (err) => {
      if (err) throw err;
    });
  });
});
