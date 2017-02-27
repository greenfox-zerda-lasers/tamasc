'use strict';

const test = require('tape');
const Nyaralas  = require('./emarsys_nyaral.js');


test('returns an array of destenations with 4 elements', function (t) {
  const horvat = new Nyaralas('4 => 3', '3 => 2', '2 => 1');

  const actual = horvat.showPath();

  t.ok(actual.length === 4);
  t.end();
});

test('with full of dependent destenations return in a correct way', function (t) {
  const horvat = new Nyaralas('4 => 3', '3 => 2', '2 => 1');

  var actual = horvat.showPath();
  var expected = ['1', '2', '3', '4'];

  t.deepEqual(actual, expected);
  t.end();
});

test('with circularly dependent destenations throws an error', function (t) {
  const horvat = new Nyaralas('4 => 3', '3 => 2', '2 => 1', '1 => 4');

  t.throws(horvat.showPath);

  t.end();
});
