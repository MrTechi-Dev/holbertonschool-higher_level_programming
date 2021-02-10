#!/usr/bin/node
const fs = require('fs');

let dataFile1 = '';
let dataFile2 = '';
//  Gathering data 📀
try {
  dataFile1 = fs.readFileSync(process.argv[2], 'utf8');
  dataFile2 = fs.readFileSync(process.argv[3], 'utf-8');
} catch (err) {
  console.error(err);
}
// Writting file 📂
const writeToFile = (data) => {
  fs.appendFile(process.argv[4], data + '\n', (err) => {
    if (err) {
      return console.error(err);
    }
  });
};
writeToFile(dataFile1);
writeToFile(dataFile2);
