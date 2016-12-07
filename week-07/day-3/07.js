'use strict';

var numbers = [2, 5, 11, 29, 4];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise

// ronda mint a bun...
function gimmiTrueIfPrime(inputArray) {
  return inputArray.map(function (e) {
    for (var i = 2, end = Math.floor(Math.sqrt(e)); i <= end;  i++){
      if (e % i === 0) {
        return false;
      }
    }
    return true;
  }).reduce(function (a, c) {return a && c;}, true);
}

//meg rondabb...
function gimmiTrueIfPrime2(inputArray) {
  return inputArray.map(function (e) {
    for (var i = 2, end = Math.floor(Math.sqrt(e)); i <= end;  i++){
      if (e % i === 0) {
        return false;
      }
    }
    return true;
  }).every(function(e) {return e;});
}

//pff......
function gimmiTrueIfPrime3(inputArray) {
  for (var i = 0, l = inputArray.length; i < l; i++){
    for (var j = 2, end = Math.floor(Math.sqrt(inputArray[i])); j <= end;  j++){
      if (inputArray[i] % j === 0) {
        return false;
      }
    }
  }
  return true;
}

// thanks Ricsi :)
function gimmiTrueIfPrime4(inputArray) {
  return inputArray.every(function (e) {
    for (var j = 2, end = Math.floor(Math.sqrt(e)); j <= end;  j++){
      if (e % j === 0) {
        return false;
      }
    }
    return true;
  });
}



console.log(gimmiTrueIfPrime(numbers));
console.log(gimmiTrueIfPrime2(numbers));
console.log(gimmiTrueIfPrime3(numbers));
console.log(gimmiTrueIfPrime4(numbers));
