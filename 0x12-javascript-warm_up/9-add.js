#!/usr/bin/node

let firstNumber = Number(process.argv[2]);
let secondNumber = Number(process.argv[3]);

add(firstNumber, secondNumber);

function add (a, b) {
  console.log(a + b);
}
