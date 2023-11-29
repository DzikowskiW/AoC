'use strict';
const fs = require('fs')

function p1(data) {
  let gamma = '';
  let epsilon = '';
  let ones = 0;
  for (let j=0; j< data[0].length; j++) {
    for (let i=0; i < data.length; i++) {
      ones += data[i][j] === '1' ? 1 : -1;
    }
    if (ones > 0) {
      gamma += '1';
      epsilon += '0';
    } else {
      gamma += '0';
      epsilon += '1';
    }
    ones = 0;
  }
  console.log('gamma', gamma);
  gamma = parseInt(gamma, 2);
  console.log('gamma', gamma);

  console.log('epsilon', epsilon);
  epsilon = parseInt(epsilon, 2);
  console.log('epsilon', epsilon);

  return gamma* epsilon;
}


function p2(data) {
  const oxy = [...data];
  const result = oxygen(oxy);
  const s = [...data];
  const sres = scrubber(s);
  console.log('oxygen', result);
  console.log('oxygen', parseInt(result.join(''),2));
  console.log('scrubbed', sres);
  console.log('scrubbed', parseInt(sres.join(''),2));
  return parseInt(result.join(''),2) * parseInt(sres.join(''),2);
}
// 3205048
function oxygen(data, position = 0) {
  if (position >= data[0].length) {
    throw new Error('too long position');
  }
  if (data.length === 1) return data[0];
  if (data.length === 2) return data[0][data[0].length-1] === '1' ? data[0] : data[1];

  let ones = data.reduce((ones, num) => num[position] === '1' ? ones + 1 : ones - 1, 0);
  const filtered = data.filter(d => {
    if (ones === 0) return d[position] === '1';
    if (ones > 0) return d[position] === '1';
    return d[position] === '0';
  });
  return oxygen(filtered, position+1);
}

function scrubber(data, position = 0) {
  if (position >= data[0].length) {
    throw new Error('too long position');
  }
  if (data.length === 1) return data[0];
  if (data.length === 2) return data[0][data[0].length-1] === '0' ? data[0] : data[1];

  let ones = data.reduce((ones, num) => num[position] === '1' ? ones + 1 : ones - 1, 0);
  const filtered = data.filter(d => {
    if (ones === 0) return d[position] === '0';
    if (ones > 0) return d[position] === '0';
    return d[position] === '1';
  });
  return scrubber(filtered, position+1);
}


function formatData(data) { 
  return data.split('\n').map(line => {
    return line.split('');
  })
}


fs.readFile('./03.txt', 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }
  console.log(p2(formatData(data)));
});