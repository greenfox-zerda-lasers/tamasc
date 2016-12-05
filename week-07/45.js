'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array
function shortestString(inputList){
  var shortest = inputList[0];
  for (var i = 1; i <  inputList.length; i++){
    if  (shortest.length > inputList[i].length){
      shortest = inputList[i];
    }
  }
  return shortest;
}

console.log(shortestString(names));
