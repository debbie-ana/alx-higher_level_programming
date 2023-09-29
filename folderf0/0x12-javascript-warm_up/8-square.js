#!/usr/bin/node
const process = require('process');
const arg = parseInt(process.argv[2]);
if (`${arg}` === 'NaN') {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    let str = '';
    for (let j = 0; j < arg; j++) {
      str += 'X';
    }
    console.log(str);
  }
}
