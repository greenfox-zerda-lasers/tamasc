'use strict';


var app = (function () {
   // ******private properties********
  var counter = 0;
  var audio = document.querySelector('audio');

  // **********functions**************
  var fireApp = function () {
    ajax.getSongList(addEventsToButtons);
    addEventsToButtons();
    addAudioEvents();
  };

// *************Helper***************
  var renderHelper = function(child, text, parent) {  //creates a HTML element and appends it to the given parent
    text.forEach(function(t) {
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
    var maxRowNum = document.querySelectorAll('#playlist tr').length-1;
    if (counter < 1) {
      counter = maxRowNum;
    } else if (counter > maxRowNum) {
      counter = 1;
    }
    return counter;
  };

  var setAudioSource = function (counter) {
    audio.src = document.getElementById(''+counter).src;
  }

  var setActive = function (counter) {
     var activeSong = document.querySelector('.active');
     if (activeSong) {
       activeSong.classList.remove('active');
     }
     document.getElementById(''+counter).classList.toggle('active');
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
    playPause.addEventListener('click', function () {
      var img = document.getElementById('pp');
      if (img.classList[0] === 'play') {
         img.src = './img/pause.svg';
         img.classList = ['pause'];
         console.log('before fire play() audio.paused:', audio.paused);
         console.log(audio.ended);
         audio.paused = false;
         audio.play();
         console.log('after fire play() audio.paused:',audio.paused);
         console.log(audio.ended);
      } else {
         img.src = './img/play.svg';
         img.classList = ['play'];
         console.log('before fire pause() audio.paused:',audio.paused);
         audio.pause();
         console.log('after fire pause() audio.paused:',audio.paused);
      }
      setAudioSource(counter);
      setActive(counter);
    });
  };

  var addAudioEvents = function () {
     audio.addEventListener("ended", function() {
      // if( !this.paused ) this.pause();
      document.querySelector('#forward').click();
     });
  }

// **************View****************

  var renderSongList = function (songs) {
     var row;
     songs.forEach(function(song) {
       var table = document.querySelector('tbody');
       row = document.createElement('tr');
       row.src = song.src;
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

  return {
    fire: fireApp,
    renderSongList: renderSongList,
  };

})();


var ajax = (function () {
   var getSongList = function () {
     var data;
     var xhr = new XMLHttpRequest();
     xhr.open('GET', 'http://localhost:3000/playlist-tracks', true);
     xhr.setRequestHeader('Content-Type', 'application/json');
     xhr.send('');
     xhr.onreadystatechange = function (rsp) {
       if (xhr.readyState === XMLHttpRequest.DONE) {
         data = JSON.parse(xhr.response);
         app.renderSongList(data.sort(function (a, b) {
           return a.id - b.id;
         }));
       }
     };
   };

  return {
      getSongList: getSongList
   };

})();

app.fire();
