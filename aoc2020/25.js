const a1 = 9232416
const b1 = 14144084
const a2 = 17807724
const b2 = 5764801

function root(a) {
    const bigseven = BigInt(7);
    const bigmod = BigInt(20201227)
    for (let i=BigInt(8927518); i< 10000000;i++) {
        if (bigseven**i % bigmod === a) return i;
    }
}

function r(a) {
    let i= 0;
    let v = 1;
    while(true){
        i++;
        v = 7*v % 20201227
        if (v === a) return i
    }
}

function t(v, r) {
    let res = 1;
    for (let i=0; i<r; i++) {
        res = res*v % 20201227
    }
    return res;
}

const ra = r(a1)
console.log('root A', ra);
//console.log('B', b1**ra % 20201227 );
// const rb = r(b2)
// console.log('root B', rb);
 console.log('A', t(b1,ra) );
