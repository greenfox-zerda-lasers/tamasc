'use strict';


var app = (function () {
  var fireApp = function () {
    ajax.getSongList(addEventsToButtons);
    addEventsToButtons();
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
    return minutes + ':' + seconds;
  }

  var counterValidator = function (counter) {
    var maxRowNum = document.querySelectorAll('#playlist tr').length-1;
    if (counter < 1) {
      counter = maxRowNum;
    } else if (counter > maxRowNum) {
      counter = 0;
    }
    return counter;
  }

// *************Events***************

var addEventsToButtons = function () {
  var counter = 1;
  var forward = document.querySelector('#forward');
  forward.addEventListener('click', function() {
    counter = counterValidator(counter-1);
    console.log(counter);
    document.querySelector('audio').src = document.getElementById(''+counter).src;
  });
};

// **************View****************

  var renderSongList = function (songs) {
     var row;
     songs.forEach(function(song) {
       var table = document.querySelector('tbody');
       row = document.createElement('tr');
       row.src = song.src;
       row.addEventListener('click', function() {
        var activeSong = document.querySelector('.active');
         if (activeSong) {
           activeSong.classList.remove('active');
         }
         this.classList.toggle('active');
         document.querySelector('audio').src = this.src;
       });
       row = renderHelper('td', [song.id, song.artist[0] + ' - ' + song.title, secToDuration(song.duration)], row);
       row.id = song.id;
       table.appendChild(row);
     });
     document.getElementById('1').classList.add('active');
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
