'use strict';

var numbers = [7, 5, 8, -1, 2, -3];
// Write a function that returns the minimal element
// in an array (your own min function)

function myMin(inputList){
  var min = inputList[0];
  for (var i = 1; i <  inputList.length; i++){
    if  (min > inputList[i]){
      min = inputList[i];
    }
  }
  return min;
}

console.log(myMin(numbers));
