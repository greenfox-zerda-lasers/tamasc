'use strict';

var express = require('express');
var bodyParser = require('body-parser');
var mysql = require('mysql');

var app = express();
app.use(bodyParser.json());
var urlencodedParser = bodyParser.urlencoded({ extended: false });

app.listen(3000);

// ***********set up DB connection *************

var connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "alma",
  database: "todo",
});

connection.connect(function(error){
  if(error){
    console.log('jajj', error.toString());
    return;
  }
  console.log('siker!');
});

// ***********  handling requests *************

app.get('/todos', function a(req, res) {
  connection.query('SELECT * FROM todos;', function(err,rows){
    console.log(rows);
    if(err) {
      console.log(err.toString());
      connection.end();
      return;
    }
    res.send(rows);
  });
});


app.post('/todos', urlencodedParser, function(req, res) {
  var completed = +Boolean(req.body.completed);
  connection.query('INSERT INTO todos (text, completed) VALUES ("'
    +req.body.text+'", "'+completed+'");',
    function(err, insertParam){
      if(err) {
        console.log(err.toString());
        connection.end();
        return;
      }
      getTodoById(insertParam.insertId, function(rows) {
        res.status(200).json(rows);
      });
    });
});

app.put('/todos/:id', urlencodedParser, function(req, res) {
  var completed = +Boolean(req.body.completed);
  connection.query('UPDATE todos SET text="'+req.body.text+'", '
    +'completed="'+completed+'" WHERE todos.id='+req.params.id+';',
    function(err){
      if(err) {
        console.log(err.toString());
        connection.end();
        return;
      }
      getTodoById(req.params.id, function(rows) {
        res.status(200).json(rows);
      });
    });
});


app.post('/todos', urlencodedParser, function(req, res) {
  var completed = +Boolean(req.body.completed);
  connection.query('INSERT INTO todos (text, completed) VALUES ("'
    +req.body.text+'", "'+completed+'");',
    function(err, insertParam){
      if(err) {
        console.log(err.toString());
        connection.end();
        return;
      }
      getTodoById(insertParam.insertId, function(rows) {
        console.log(rows);
      });
      getTodoById(insertParam.insertId, function(rows) {
        res.status(200).json(rows);
      });
    });
});

// ***********  helper functions *************

function getTodoById(id, callback) {
  connection.query('SELECT * FROM todos WHERE todos.id='+id+';', function(err,rows){
    if(err) {
      console.log(err.toString());
      connection.end();
      return;
    }
    callback(rows);
  });
}
