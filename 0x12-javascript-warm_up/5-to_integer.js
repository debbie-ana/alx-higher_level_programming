#!/usr/bin/node
const process = require('process');
const arg = parseInt(process.argv[2]);
if (`${arg}` === 'NaN') {
  console.log('Not a number');
} else {
  console.log('My number: ' + `${arg}`);
}
