'use strict';
const fs = require('fs')

function p1(data) {
  const result = 0;
  return data;
}

function p2(data) {
  const result = 0;
  return result;
}


fs.readFile('./01.txt', 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }
  let sum =0;
  let maxSum = 0;
  let sums = []
  data = data.split('\n')
  data.forEach(d => {
    if (d.length === 0) {
      sums.push(sum)
      maxSum = sum > maxSum ? sum : maxSum;
      sum = 0;
    } else {
      sum += parseInt(d, 10)
    }
  });  
  sums.sort(function(a, b) {
    return b- a;
  })
  console.log(sums)
  console.log(sums[0] + sums[1]+sums[2]);

});