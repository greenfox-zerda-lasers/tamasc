'use strict';

var numbers = [2.4, 3.5, 1.7, 3.3, 1.2];

// create a function that takes an array of numbers,
// it should return a new array that consists only the numbers that are
// bigger than 2 and all of it's elements should be rounded

function roundB2(inputArray) {
  return inputArray.map(function(e) {if (e>2) {return Math.round(e);} return e;});
}

console.log(roundB2(numbers));
