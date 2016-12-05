'use strict';

// create a function that returns it's input factorial

function myFactorial(inputInt){
  var factorial = 1;
  for (var i = 1; i <= inputInt; i++){
    factorial *= i;
  }
  return factorial;
}

console.log(myFactorial(5));
