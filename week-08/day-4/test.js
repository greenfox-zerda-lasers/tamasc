'use strict';

var test = require('tape');

var double_input = require('../../week-07/day-1/39.js');
var appendA = require('../../week-07/day-1/40.js');
var mySum = require('../../week-07/day-1/41.js');
var myFactorial = require('../../week-07/day-1/42.js');
var evenNums = require('../../week-07/day-1/43.js');
var myMin = require('../../week-07/day-1/44.js');
var shortestString = require('../../week-07/day-1/45.js');


test('returns the shortest string in a list', function (t) {
    var actual = double_input(23);
    var expected = 46;

    t.equal(actual, expected);
    t.end();
});

test('adding an "a" to the end of string', function (t) {
    var actual = appendA('kuty');
    var expected = 'kutya';

    t.equal(actual, expected);
    t.end();
});

test('adding an "a" to the end of int', function (t) {
    var actual = appendA(5);
    var expected = '5a';

    t.equal(actual, expected);
    t.end();
});

test('sum of [1, 2, 3, 4, 5]', function (t) {
    var arr = [1, 2, 3, 4, 5];

    var actual = mySum(arr);
    var expected = arr.reduce(function (a, e) {
      return a + e;
    });

    t.equal(actual, expected);
    t.end();
});

test('sum of long array', function (t) {
    var arr = [1, 2, 3, 4, 5, 56, 34, 24, 213123, 34, 54, 45, 65, 657];

    var actual = mySum(arr);
    var expected = arr.reduce(function (a, e) {
      return a + e;
    });

    t.equal(actual, expected);
    t.end();
});

test('factorial of 10', function (t) {
    var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    var actual = myFactorial(10);
    var expected = arr.reduce(function (a, e) {
      return a * e;
    }, 1);

    t.equal(actual, expected);
    t.end();
});

test('min of numbers', function (t) {
    var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    var actual = myMin(arr);
    var expected = 1;

    t.deepEqual(actual, expected);
    t.end();
});

test('min of numbers', function (t) {
    var arr = ['1', 'asdasd', 'asd', '4', 'afdsagsdgsad', 'sadfdff', 'sf'];

    var actual = shortestString(arr);
    var expected = '1';

    t.deepEqual(actual, expected);
    t.end();
});
