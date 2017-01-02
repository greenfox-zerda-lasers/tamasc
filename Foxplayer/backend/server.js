'use strict';

var cors = require('cors');
var express = require('express');
var bodyParser = require('body-parser');
var data = require('./data.json');

var app = express();
app.use(bodyParser.json());
app.use(cors());
var urlencodedParser = bodyParser.urlencoded({ extended: false });

var fs = require('fs');
var mm = require('musicmetadata');


app.get('/', function a(req, res) {
  var songList = [];
  for (var i = 0, l = data.songs.length; i < l; i++){
    console.log(data.songs[i].url);
    var stream = fs.createReadStream(data.songs[i].url);
    var parser = mm(stream, function (err, metadata) {
      if (err) throw err;
      songList.push(metadata);
      if (data.songs.length == songList.length) {
        res.send(songList);
      }
      stream.close();
    });
  }
});



app.listen(3000);
