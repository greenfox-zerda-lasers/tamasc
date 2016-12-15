'use strict';

var numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens

function evenNums(array) {
  return array.filter(function(item){
    if (item % 2 === 0){return item;}
  });
}


module.exports = evenNums;
