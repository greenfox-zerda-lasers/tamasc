'use strict';

var express = require('express');

var app = express();

var data = [
  {
      "completed": false,
      "id": 1,
      "text": "Buy milk"
  },
  {
      "completed": false,
      "id": 2,
      "text": "Make dinner"
  },
  {
      "completed": false,
      "id": 3,
      "text": "Save the world"
  }
];

app.get('/todos', function a(req, res) {
  res.set('Content-Type', 'application/json');
  res.send(JSON.stringify(data));
});

app.get('/:id', function a(req, res) {
  res.set('Content-Type', 'application/json');
  res.send(
    JSON.stringify(data.filter(function(e) {
      return parseInt(req.params.id) === e["id"];
    }))
  );
});

app.get('/*', function a(req, res) {
  console.log(req.url);
  res.send(String(new Date()) + ' \nhajajajajajajjjjj\n' + req.url);
});

app.listen(3000);
