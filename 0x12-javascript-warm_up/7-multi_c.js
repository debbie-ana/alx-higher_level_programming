#!/usr/bin/node
const process = require('process');
const arg = parseInt(process.argv[2]);
if (`${arg}` === 'NaN') {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arg; i++) {
    console.log('C is fun');
  }
}
