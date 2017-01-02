'use strict';

var express = require('express');
var bodyParser = require('body-parser');
var mysql = require('mysql');

var app = express();
app.use(bodyParser.json());
var urlencodedParser = bodyParser.urlencoded({ extended: false });


var connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "alma",
  database: "bookstore",
});

connection.connect(function(error){
  if(error){
    console.log('jajj', error.toString());
    return;
  }
  console.log('siker!');
});

app.get('/', function(req, res) {
  connection.query('SELECT book_name FROM book_mast;', function(err,rows){
    if(err) {
      console.log(err.toString());
      connection.end();
      return;
    }
    res.send(rows);
  });
});

app.get('/:bId', function(req, res) {
  connection.query('SELECT book_name FROM book_mast WHERE book_id="BK'+req.params.bId+'";',
    function(err,rows){
      console.log('SELECT book_name FROM book_mast WHERE book_id="BK'+req.params.bId+'";');
      if(err) {
        console.log(err.toString());
        connection.end();
        return;
      }
      res.send(rows);
    });
});

app.listen(3000);
