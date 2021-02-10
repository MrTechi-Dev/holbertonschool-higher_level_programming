#!/usr/bin/node
// computes a dictionary of user ids by occurrence.
const { dict } = require('./101-data');
const newdict = {};
for (const key in dict) {
  if (dict[key] in newdict) {
    newdict[dict[key]].push(key);
  } else {
    newdict[dict[key]] = [key];
  }
}
console.log(newdict);
