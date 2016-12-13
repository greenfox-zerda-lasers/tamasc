// Create a "tour" function that takes two functions as parameters:
//  - walk and distance
//  - distance should return an array of false values [false,false,false]
// with the length of a given parameter
//  - walk should go through the returned array of distance and change it to true
//  - tour should return the result of walk

function tour(walk, distance) {
  var length = 5;
  return walk(distance(length));
}

function distance(length) {
  var arr = [];
  for (var i = 0; i < length; i++) {
    arr.push(false);
  }
  return arr;
}

function walk(arr) {
  return arr.map(function(e) {
    return !e;
  });
}

console.log(tour(walk, distance));
