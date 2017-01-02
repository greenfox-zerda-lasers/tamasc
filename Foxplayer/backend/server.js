'use strict';

var cors = require('cors');
var express = require('express');
var bodyParser = require('body-parser');
var data = require('./data.json');

var app = express();
app.use(bodyParser.json());
app.use(cors());
var urlencodedParser = bodyParser.urlencoded({
    extended: false
});

var fs = require('fs');
var mm = require('musicmetadata');


app.get('/', function a(req, res) {
    var songList = [];
    for (var i = 0, l = data.songs.length; i < l; i++) {
        (function(e) { // was a reference problem!!!!!!!
            var stream = fs.createReadStream(data.songs[e].url);
            var parser = mm(stream, {
                duration: true
            }, function(err, metadata) {
                if (err) throw err;
                metadata.id = data.songs[e].id;
                metadata.src = data.songs[e].url;
                songList.push(metadata);
                if (data.songs.length == songList.length) {
                    res.send(songList);
                }
                stream.close();
            });
        })(i)
    };
});



app.listen(3000);
