'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var students = {
  grades: [],
  addGrade: function () {
    if (arguments){
      for (var i = 0, l = arguments.length; i < l; i++){
        if (arguments[i] < 6 && arguments[i] > 0){this.grades.push(arguments[i]);}
      }
    }
  },
  getAverage: function () {
    return this.grades.reduce(function (a, c) {return a + c;}, 0)/this.grades.length;
  }
};

students.addGrade(5, 3, 9, 4);
students.addGrade(1, 3, -1);
students.addGrade(3);
students.addGrade(2);

console.log(students.grades);
console.log(students.getAverage());
