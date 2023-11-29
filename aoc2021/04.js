'use strict';
const fs = require('fs')

function p1(data) {
  console.log(data);
}

function p2(data) {

}

function formatData(data) { 
  let bingos = data.split('\n\n');
  const draws = bingos.shift().split(',').map(val => parseInt(val, 10));
  bingos = bingos.map(
    bingo => bingo
      .split('\n')
      .map(
        l => l
          .split(/\s+/)
          .filter(el => el != '')
          .map( el => parseInt(el, 10))
      )
  )
  return { draws, bingos };
}


fs.readFile('./04.txt', 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }
  data = formatData(data);
  console.log(p1(data));
});