'use strict';
const { assert } = require('console');
const fs = require('fs')

function p1(data) {
  const result = 0;
  return data;
}

function p2(data) {
  const result = 0;
  return result;
}

const BONUS = {'X': 1, 'Y':2, 'Z': 3};
const BONUS2 = {'X': 1, 'Y':2, 'Z': 3};

fs.readFile('./02.txt', 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }
  let val = 0;
  data = data.split('\n')
  data.forEach(d => {
    let v =0;
    let c = d.charCodeAt(0) + 23;
    let neededRes = d[2];
    if (neededRes === 'X') {
      v += 0
      c += 2;
    } else if (neededRes === 'Y'){
      v += 3
    } else {
      v += 6
      c += 1
    }
    if (c > 'Z'.charCodeAt(0)) c -=3;
    

    console.log(d[0], String.fromCharCode(c), v);

    val += v + BONUS2[String.fromCharCode(c)];
  });  
 
  console.log(val)

});


// fs.readFile('./02.txt', 'utf8', function (err,data) {
//   if (err) {
//     return console.log(err);
//   }
//   let val = 0;
//   data = data.split('\n')
//   data.forEach(d => {
//     let res = d.charCodeAt(0) % 3 - (d.charCodeAt(2)-23) % 3;
//     let v = BONUS[d[2]];
//     if (res < 0) res = 3 + res;
    
//     if (res === 0 ) {
//       //tie
//       v += 3
//     }
//     else if (res === 1 ) {
//       //lose
//       v += 0
//     } 
//     else if (res === 2) {
//       // win
//       v += 6
//     } 
//     else assert('invalid value', res);
//     val += v;
//   });  
 
//   console.log(val)

// });