'use strict';

const test = require('tape');
const Holiday  = require('./emarsys_nyaral.js');


test('returns an array of destenations with 4 elements', function (t) {
  const horvat = new Holiday('4 => 3', '3 => 2', '2 => 1');

  const actual = horvat.showPath();

  t.ok(actual.length === 4);
  t.end();
});

test('with full of dependent destenations returns the correct order', function (t) {
  const horvat = new Holiday('4 => 3', '3 => 2', '2 => 1');

  const actual = horvat.showPath();
  const expected = ['1', '2', '3', '4'];

  t.deepEqual(actual, expected);
  t.end();
});

test('with circularly dependent destenations throws an error', function (t) {
  const horvat = new Holiday('4 => 3', '3 => 2', '2 => 1', '1 => 4');

  t.throws(horvat.showPath);
  t.end();
});

test('with full of dependent and with an independent destenation at the begining returns the correct order', function (t) {
  const horvat = new Holiday('h', '4 => 3', '3 => 2', '2 => 1');

  const actual = horvat.showPath();
  const expected = ['1', '2', '3', '4', 'h'];

  t.deepEqual(actual, expected);
  t.end();
});

test('with full of dependent and with an independent destenation at the end returns the correct order', function (t) {
  const horvat = new Holiday('4 => 3', '3 => 2', '2 => 1', 'h');

  const actual = horvat.showPath();
  const expected = ['1', '2', '3', '4', 'h'];

  t.deepEqual(actual, expected);
  t.end();
});

test('with full of dependent and with an independent destenation at the middle returns the correct order', function (t) {
  const horvat = new Holiday('4 => 3', '3 => 2', 'h', '2 => 1');

  const actual = horvat.showPath();
  const expected = ['1', '2', '3', '4', 'h'];

  t.deepEqual(actual, expected);
  t.end();
});

test('with mix of dependent and independent destenations returns the correct order', function (t) {
  const horvat = new Holiday('4 => 3', 'h', '2 => 1', 'h', 'y','3 => 2', 'l');

  const actual = horvat.showPath();
  const expected = ['1', '2', '3', '4', 'l', 'y', 'h'];

  t.deepEqual(actual, expected);
  t.end();
});

test('with a destenation having 2 dependencies returns a correct and possible path', function (t) {
  const horvat = new Holiday('4 => 3', '3 => 2', '2 => 1', '4 => 2');

  const actual = horvat.showPath();

  t.ok(actual.length >= 3);
  t.end();
});
