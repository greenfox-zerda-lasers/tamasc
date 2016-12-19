'use strict';

var express = require('express');

var exampleApp = express();

exampleApp.get('/', function(req, res) {
  res.send('hellobello');
});

exampleApp.post('/', function(req, res) {
  res.send('post hellobello');
});

exampleApp.listen(3000);
