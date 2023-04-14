#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += 'X';
      }
      console.log(`${str}`);
    }
  }

  rotate () {
    let wd = this.width;
    this.width = this.height;
    this.height = wd;
  }
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
