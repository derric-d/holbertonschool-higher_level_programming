#!/usr/bin/node
const iDict = require('./101-data').dict;
const nDict = {};
for (const k of Object.keys(iDict)) {
  if (!(iDict[k] in nDict)) {
    nDict[iDict[k]] = [k];
  } else {
    nDict[iDict[k]].push(k);
  }
}
console.log(nDict);
