#!/usr/bin/node
const process = require('process');
if (process.argv.length <= 3) {
  console.log('0');
} else {
  let slg = process.argv[2];
  let lg = 0;
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > lg) {
      slg = lg;
      lg = process.argv[i];
    } else if ((process.argv[i] !== lg) && (process.argv[i] > slg)) {
      slg = process.argv[i];
    }
  }
  console.log(slg);
}
