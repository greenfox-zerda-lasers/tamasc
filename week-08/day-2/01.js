'use strict';

// create a function that when called alerts "I'm delayed" after 1 second
var alert1 = function() {
  setTimeout(function() {alert('I\'m delayed')}, 1000);
};
