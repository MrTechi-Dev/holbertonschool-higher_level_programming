#!/usr/bin/node

const firstNumber = Number(process.argv[2]);
const secondNumber = Number(process.argv[3]);

add(firstNumber, secondNumber);

function add (a, b) {
  console.log(a + b);
}
