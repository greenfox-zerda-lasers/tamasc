'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}

function countLetters(inputString) {
  var o = {};
  var strArray = inputString.split('');
  strArray.forEach(function (letter){
    if (!o[letter]) {
      o[letter] = 1;
    } else {
      o[letter] += 1;
    }
  });
  return o;
}

console.log(countLetters('asdasd sad asijjhds fds fsd f'));
