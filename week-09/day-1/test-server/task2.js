'use strict';

var express = require('express');
var bodyParser = require('body-parser');
var data = require('./data.json');

var app = express();
app.use(bodyParser.json());
var urlencodedParser = bodyParser.urlencoded({ extended: false });


app.get('/todos', function a(req, res) {
  res.set('Content-Type', 'application/json');
  res.send(JSON.stringify(data));
});

app.get('/:id', function a(req, res) {
  res.set('Content-Type', 'application/json');
  res.send(
    data.filter(function(e) {
      return parseInt(req.params.id) === e["id"];
    })
  );
});

app.get('/*', function a(req, res) {
  console.log(req.url);
  res.send(String(new Date()) + ' \nhajajajajajajjjjj\n' + req.url);
});

app.post('/todos', urlencodedParser, function a(req, res) {
  console.log(req.body);
  var todo = {
    completed: Boolean(req.body.completed),
    id: data.length+1,
    text: req.body.text,
  };
  data.push(todo);
  res.send(JSON.stringify(todo));
});

app.listen(3000);
