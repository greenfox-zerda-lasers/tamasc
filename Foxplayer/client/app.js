'use strict';


var app = (function () {
  // ******private properties********
  var counter = 0;
  var audio = document.getElementsByTagName('audio')[0];
  var imgPP = document.getElementById('pp'); //play-pause button
  var imgArtist = document.getElementById('imgArtist');
  // **********functions**************
  var fireApp = function () {
    ajax.getSongList(addEventsToButtons);
    addEventsToButtons();
    // addAudioEvents();
  };

  // *********Helper functions***********
  var renderHelper = function (child, text, parent) { //creates a HTML element and appends it to the given parent
    text.forEach(function (t) {
      var childElement = document.createElement(child);
      childElement.innerText = t;
      parent.appendChild(childElement);
    });
    return parent;
  };

  var secToDuration = function (sumSec) {
    var minutes = Math.floor(sumSec / 60);
    var seconds = Math.floor(sumSec % 60);
    if (seconds < 10) {
      seconds = '0' + seconds;
    }
    return minutes + ':' + seconds;
  };

  var counterValidator = function (counter) {
    var maxRowNum = document.querySelectorAll('#playlist tr').length - 1;
    if (counter < 1) {
      counter = maxRowNum;
    } else if (counter > maxRowNum) {
      counter = 1;
    }
    return counter;
  };

  var setAudioSource = function (counter) {
    audio.src = document.getElementById('' + counter).src;
  }

  var setActive = function (counter) {
    var activeSong = document.querySelector('.active');
    if (activeSong) {
      activeSong.classList.remove('active');
    }
    var currentSong = document.getElementById('' + counter);
    currentSong.classList.toggle('active');
    var currentSongText = document.querySelectorAll('.active > td')[1].innerText;
    imgPP.src = './img/pause.svg';
    imgPP.classList = ['pause'];
    renderCurrentSong(currentSongText, currentSong.artist[0]);
  };

  var togglePlayPause = function () {
    if (!audio.paused) {
      audio.pause();
      imgPP.src = './img/play.svg';
      imgPP.classList = ['play'];
    } else {
      audio.play()
      imgPP.src = './img/pause.svg';
      imgPP.classList = ['pause'];
    };
  };

  // *************Events***************

  var addEventsToButtons = function () {
    var forward = document.querySelector('#forward');
    forward.addEventListener('click', function () {
      counter = counterValidator(counter + 1);
      setAudioSource(counter);
      setActive(counter);
    });

    var backward = document.querySelector('#backward');
    backward.addEventListener('click', function () {
      counter = counterValidator(counter - 1);
      setAudioSource(counter);
      setActive(counter);
    });

    var playPause = document.querySelector('#play-pause');
    playPause.addEventListener('click', togglePlayPause)
  };

  var addAudioEvents = function () {
    audio.addEventListener("ended", function () {
      if (!this.paused) this.pause();
      document.querySelector('#forward').click();
      audio.play();
    });
  };

  // **************View****************
  var renderSongList = function (songs) {
    var row;
    songs.forEach(function (song) {
      var table = document.querySelector('.tracks');
      row = document.createElement('tr');
      row.src = song.src;
      row.artist = song.artist;
      row.addEventListener('click', function () {
        counter = parseInt(counterValidator(this.id));
        setActive(counter);
        audio.src = this.src;
      });
      row = renderHelper('td', [song.id, song.artist[0] + ' - ' + song.title, secToDuration(song.duration)], row);
      row.id = song.id;
      table.appendChild(row);
    });
  };

  var renderCurrentSong = function (currentSongText, artist) {
    var currentSongEl = document.querySelector('.song-info');
    currentSongEl.innerText = currentSongText;
    ajax.getArtistInfo(artist);
  };

  return {
    fire: fireApp,
    renderSongList: renderSongList,
  };

})();


var ajax = (function () {
  var open = function (request, url, dataToSend, callback) {
    var data;
    var xhr = new XMLHttpRequest();
    xhr.open(request, url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(dataToSend);
    xhr.onreadystatechange = function (rsp) {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        data = JSON.parse(xhr.response);
        callback(data);
      }
    };
  };

  var getSongList = function () {
    var renderSongList = function (data) {
      app.renderSongList(data.sort(function (a, b) {
        return a.id - b.id;
      }));
    };
    open('GET', 'http://localhost:3000/playlist-tracks', '', renderSongList)
  };

  var getArtistInfo = function (artist) {
    var changeImg = function (data) {
      imgArtist.src = data.artist.image[2]['#text'];
      if (!data.artist.image[2]['#text']) {
        imgArtist.src = 'https://raw.githubusercontent.com/greenfox-academy/teaching-materials/master/javascript/project-music-player/img/music-placeholder.png';
      }
    };
    var url = 'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=' + artist +
      '&api_key=ee125f318852fc7d1c2f4e21458a0035&format=json'
    open('GET', url, '', changeImg)
  };

  return {
    getSongList: getSongList,
    getArtistInfo: getArtistInfo
  };

})();

app.fire();
