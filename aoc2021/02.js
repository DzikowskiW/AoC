'use strict';
const fs = require('fs')

function p1(data) {
  const fwd = data.map(({dir, num}) => {
    if (dir === 'forward') return num;
    return 0;
  }).reduce((sum, cur) => sum + cur, 0);
  console.log('fwd', fwd);

  const depth = data.map(({dir, num}) => {
    if (dir === 'down') return num;
    if (dir === 'up') return -num;
    return 0;
  }).reduce((sum, cur) => sum + cur, 0);

  return Math.abs(fwd)*Math.abs(depth);
}

function p2(data) {
  let fwd = 0;
  let depth = 0;
  let aim = 0;

  data.forEach(({dir, num}) => {
    if (dir === 'forward') {
      fwd += num;
      depth += aim*num;
    }
    if (dir === 'up') {
      //depth -= num;
      aim -= num;
    }
    if (dir === 'down') {
      //depth += num;
      aim += num;
    }
  })
  console.log('fwd', fwd);
  console.log('d', depth);
  return Math.abs(fwd)*Math.abs(depth);

}


fs.readFile('./02.txt', 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }
  data = data.split('\n').map(d => {
    let [dir, num] = d.split(' ');
    return {
      dir, 
      num: parseInt(num, 10),
    };
  });
  console.log(p2(data));
});