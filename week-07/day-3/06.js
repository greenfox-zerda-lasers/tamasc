'use strict';


// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise

function gimmiTrue(inputString, letter) {
  var x = false;
  inputString.split('').forEach(function (e) {
    if (e === letter) {
      x = true;
    }
  });
  return x;
}


function gimmiTrue2(inputString, letter) {   //reffering to Bence
  return inputString.split('').indexOf(letter) != -1;
}




console.log(gimmiTrue('adsas sad fasf asfafsasfasf', 'a'));
console.log(gimmiTrue2('adsas sad fasf asfafsasfasf', 'a'));
