'use strict';
const fs = require('fs')

function p2(data, size = 1000000, rounds = 10000000) {
  data = data.split('').map(d => parseInt(d,10));
  let state = [...Array(size).keys()].map((v,i) => i < data.length ? data[i] : i +1);

  let prev = null;
  let d = new Map();
  let start;
  state.forEach((v) => {
    if (prev === null) start = v;
    else {
      d.set(prev, v);
    }
    prev = v;
  });
  d.set(state[state.length-1], start);
  let current = start;
  let len = d.size;
  while (rounds-- > 0) {
    let a = d.get(current);
    let b = d.get(a);
    let c = d.get(b);
    let next = d.get(c);
    d.set(current, next);
    let dest = current;
    while (true) {
      dest--;
      if (dest === 0) dest = len;
      if (![a,b,c].includes(dest)) break;
    } 
    d.set(c,d.get(dest));
    d.set(dest, a);
    current = next;
  }

  current = 1;
  while (d.get(current) != 1) current = d.get(current);
  console.log(d.get(current));
  console.log(d.get(d.get(current)));
  console.log(d.get(d.get(d.get(current))));
}


fs.readFile('./22.txt', 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }
  p2(data);
  //p2(data, 9, 10);
});