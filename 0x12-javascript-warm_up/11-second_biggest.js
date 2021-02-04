#!/usr/bin/node
if (!process.argv[2] || process.argv.length === 3) {
  console.log(0);
} else {
  const array = process.argv.slice(2).sort((a, b) => a - b);
  // using spread operator
  // let [a, b, ...array] = process.argv.sort();
  console.log(array[array.length - 2]);
}
