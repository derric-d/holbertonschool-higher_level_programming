#!/usr/bin/node
const num = Number(process.argv[2]);
let sq = '';
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      sq += 'X';
    }
    if (i !== num - 1) {
      sq += '\n';
    }
  }
  console.log(sq);
}
