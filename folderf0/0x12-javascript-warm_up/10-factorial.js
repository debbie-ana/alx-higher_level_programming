#!/usr/bin/node
const process = require('process');

function factorial (num) {
  if (num < 2 || `${num}` === 'NaN') {
    return (1);
  }
  return (num * factorial(num - 1));
}

const a = parseInt(process.argv[2]);
console.log(`${factorial(a)}`);
