#!/usr/bin/node
const process = require('process');
let args = process.argv;
if (args.length < 3)
{
	console.log('No argument');
} else if (args.length < 4) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
