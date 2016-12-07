'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods

function Stack () {
  this.elements = [];
  this.size = function() {
    return this.elements.length;
  };
  this.push = function (element){
    this.elements[this.elements.length] = element;
  };
  this.pop = function () {
    var lastElement = this.elements[this.elements.length - 1];
    this.elements.length = this.elements.length - 1;
    return lastElement;
  };
}

var x = new Stack();
x.push(1);
x.push(4);
x.push(4);
x.push(5);
console.log(x.elements);
var v = x.pop();
console.log(x.elements);
console.log(v);
