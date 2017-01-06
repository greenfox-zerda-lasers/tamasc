'use strict';

let data = require('../data/data2.json');

const cors = require('cors');
const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const mm = require('musicmetadata');

const app = express();
app.use(bodyParser.json());
app.use(cors());

const urlencodedParser = bodyParser.urlencoded({
  extended: false,
});


app.get('/playlist-tracks', function (req, res) {
  let songList = [];
  let i = 0;
  const l = data.songs.length;
  for (i; i < l; i++) {
    (function (e) {                                     // was a reference problem!!!!!!!
      const stream = fs.createReadStream(data.songs[e].url);
      mm(stream, {
        duration: true,
      }, function (err, metadata) {
        if (err) throw err;
        metadata.id = data.songs[e].id;
        metadata.src = data.songs[e].url;
        songList.push(metadata);
        if (data.songs.length === songList.length) {
          res.send(songList);
        }
        stream.close();
      });
    })(i);
  }
});

app.get('/playlist-tracks/:playlist_id', function (req, res) {
  res.json(data);
});

app.get('/playlist', function (req, res) {
  res.json(data.playlists);
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
