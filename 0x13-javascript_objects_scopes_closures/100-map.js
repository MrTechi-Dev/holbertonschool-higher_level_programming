#!/usr/bin/node
const { list } = require('./100-data');
const doubleList = list.map((element, index) => element * index);
console.log(list);
console.log(doubleList);
