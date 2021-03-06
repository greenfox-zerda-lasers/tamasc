'use strict';

const binarySearch = function (array, number) {
  let N = array.length - 1;
  let lowerBound = 0;
  let upperBound = N;
  if (number === array[lowerBound] || number === array[upperBound]) {
    return true;
  }
  while (lowerBound !== upperBound ) {
    let M = Math.floor((lowerBound + upperBound)/2);
    console.log(lowerBound, upperBound, M);
    if (array[M] == number) {
      return true;
    } else {
      if (array[M] > number) {
        upperBound = Math.ceil((lowerBound + upperBound)/2);
      } else {
        lowerBound = M;
      }
    }
  }
  return false;
}

let arr = require('./array.js');
const x = 1;

const start = new Date();
console.log(binarySearch(arr, x));
const end = new Date();
console.log(end - start);
