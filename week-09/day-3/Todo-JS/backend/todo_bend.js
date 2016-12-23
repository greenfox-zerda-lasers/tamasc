'use strict';

var cors = require('cors');
var express = require('express');
var bodyParser = require('body-parser');
var mysql = require('mysql');

var app = express();
app.use(bodyParser.json());
app.use(cors());
var urlencodedParser = bodyParser.urlencoded({ extended: false });

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
      getTodoById(insertParam.insertId, res, function(rows) {
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
      getTodoById(req.params.id, res, function(rows) {
        res.status(200).json(rows);
      });
    });
});


app.delete('/todos/:id', urlencodedParser, function(req, res) {
  getTodoById(req.params.id, res, function(rows) {

    rows[0].destroyed = true;
    connection.query('DELETE FROM todos WHERE todos.id='+req.params.id+';',
      function(err){
        if(err) {
          console.log(err.toString());
          connection.end();
          return;
        }
      });
      res.status(200).json(rows);
  });
});

// ***********  helper functions *************

function getTodoById(id, res, callback) {
  connection.query('SELECT * FROM todos WHERE todos.id='+id+';', function(err,rows){
    if(err) {
      console.log(err.toString());
      connection.end();
      return;
    }
    if (!rows.length) {
      res.status(404).send('Nincs!!!!!!!!!!!!!!!');
      return;
    }
    callback(rows);
  });
}

app.listen(3000);
