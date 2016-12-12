'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangle(side1, side2) {
  this.side1 = side1;
  this.side2 = side2;
}

Rectangle.prototype.getArea = function () {
  return this.side1 * this.side2;
};

Rectangle.prototype.getCircumference = function () {
  return (this.side1 + this.side2) * 2;
};

var rec1 = new Rectangle(3, 4);

console.log(rec1.getCircumference());
