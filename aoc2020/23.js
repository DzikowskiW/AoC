'use strict';
const fs = require('fs')

function findTile(input) {
    const t = {
        h: 0,
        dl:0,
        dr:0 
    };
    let i = 0;
    while (i < input.length) {
        let c = input[i++];
        if (c === 's' || c === 'n') {
            c += input[i++];
        }
        switch (c) {
            case 'e': t.h -= 1; break;
            case 'w': t.h += 1; break;
            case 'ne': t.dl += 1; break;
            case 'nw': t.dr += 1; break;
            case 'sw': t.dl -= 1; break;
            case 'se': t.dr -= 1; break;
            default: console.log("INVALID",c);
        }
    }
    const x = t.h + t.dr;
    const y = t.dl + t.dr;
    return `${x}x${y}`;

    //return `h${t.h}dl${t.dl}dr${t.dr}`;
}

function makeGrid(tiles) {
    const rounds = 100;
    while (rounds-- > 0) {
        const oldTiles = [...tiles];
        const neighborsMap = new Map();
        const tilesMap = new Map();
        tiles.forEach(t => {
            const txy = t.split('x').map(Number);
            // mark surrounding tiles
            neighborsMap.set()
            // 
        });
    }
}

fs.readFile('./23a.txt', 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }

  data = data.split('\n').map(findTile);
  const map = new Map();
  data.forEach(d => map.has(d) ? map.set(d, !map.get(d)) : map.set(d, true));
  console.log(Array.from(map.values()).filter(v => v).length);



});