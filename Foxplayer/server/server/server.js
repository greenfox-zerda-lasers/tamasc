'use strict';

let data = require('../data/data.json');

const cors = require('cors');
const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const mm = require('musicmetadata');
const mysql = require('mysql');

const app = express();
app.use(bodyParser.json());
app.use(cors());

const urlencodedParser = bodyParser.urlencoded({
  extended: false,
});

// ***********set up DB connection *************

var connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "alma",
  database: "foxplayer",
});

connection.connect(function(error){
  if(error){
    console.log('error on connection to database', error.toString());
    return;
  }
  console.log('connected to database');
});


// ***********  handling requests *************

app.get('/playlist-tracks', function (req, res) {
  let songList = [];

  connection.query('SELECT * FROM songs;', function (err, data) {
    if(err) {
      console.log(err.toString());
      connection.end();
      return;
    }
    let i = 0;
    const l = data.length;
    for (i; i < l; i++) {
      (function (e) {                                     // was a reference problem!!!!!!!
        const stream = fs.createReadStream(data[e].url);
        mm(stream, {duration: true}, function (err, metadata) {
          if (err) throw err;
          metadata.id = data[e].id;
          metadata.src = data[e].url;
          songList.push(metadata);
          if (data.length === songList.length) {
            res.send(songList);
          }
          stream.close();
        });
      })(i);
    }
  });
});

app.get('/playlist-tracks/:playlist_id', function (req, res) {
  res.json(data);
});

app.get('/playlist', function (req, res) {
  connection.query('SELECT * FROM playlists;', function(err, data){
    if(err) {
      console.log(err.toString());
      connection.end();
      return;
    }
    res.json(data);
  });
});

app.post('/playlist', function (req, res) {
  var newPlayist = {"playlist" : "blabla"}
  res.json(newPlayist);
});

app.delete('/playlist/:id', function (req, res) {
  console.log(req.params.id);
  console.log("dsfdf");
  res.json(data);
});

app.post('/playlist-tracks/:playlist_id', function (req, res) {
  res.json(data);
});

app.delete('/playlist-tracks/:playlist_id/:track_id', function (req, res) {
  res.json(data);
});

module.exports = app;
