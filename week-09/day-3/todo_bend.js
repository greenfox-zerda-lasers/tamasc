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
  console.log(req.body);
  var completed = +Boolean(req.body.completed);
  connection.query('INSERT INTO todos (text, completed) VALUES ("'
    +req.body.text+'", "'+completed+'");',
    function(err){
      console.log(arguments);
      if(err) {
        console.log(err.toString());
        connection.end();
        return;
      }
      res.json(req.body);
    });
});
