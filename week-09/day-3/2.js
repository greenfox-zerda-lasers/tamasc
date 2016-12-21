// 'use strict';
//
// var http = require('http');
//
// var server = http.createServer(function a(req, res) {
//   res.writeHead(200, { 'Content-Type': 'text/plain' });
//   res.end(String(new Date()));
// });
//
//
// server.listen(3000, '127.0.0.1');

// ******************************************
var mysql = require("mysql");

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

connection.query("SELECT book_name, aut_name, book_price, cate_descrip, pub_name  FROM book_mast "
    +"LEFT JOIN  author ON book_mast.aut_id=author.aut_id "
    +"LEFT JOIN category ON book_mast.cate_id=category.cate_id "
    +"LEFT JOIN publisher ON book_mast.pub_id=publisher.pub_id;",
  function(error,rows){
    if (error) {
      console.log(error.toString());
      return;
    }
    console.log("Data received from Db:\n");
    rows.forEach(function(e) {
      console.log(e.aut_name+":", e.book_name+" -", e.book_price+"$", e.cate_descrip+" -", e.pub_name);
    });
  }
);

connection.end();
