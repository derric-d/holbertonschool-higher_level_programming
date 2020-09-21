#!/usr/bin/node
const list1 = require('./100-data.js').list;
console.log(list1);
const rList = list1.map((ele, index) => ele * index);
console.log(rList);
