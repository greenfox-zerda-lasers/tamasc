'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10];
// write your own sum function

function mySum(inputList){
  var sum = 0;
  for (var i = 0; i < inputList.length; i++){
    sum += inputList[i];
  }
  return sum;
}

console.log(mySum(numbers));

module.exports = mySum;
