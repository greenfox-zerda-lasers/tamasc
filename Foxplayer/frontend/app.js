'use strict';


var app = (function() {

  var logg = function (data) {
     console.log(data);
  };

  var renderSongList = function (songs) {
     var row;
     songs.forEach(function(song) {
        var table = document.querySelector('tbody');
        console.log(table);
        row = document.createElement('tr');
        row.src = song.src;
        row.addEventListener('click', function() {
         console.log();
         document.querySelector('audio').src = this.src;
        });
        row = renderHelper('td', [song.id, song.artist[0] +" - "+song.title, song.duration], row);
        table.appendChild(row);
     });
  };

  var renderHelper = function(child, text, parent) {  //creates a HTML element and appends it to the given parent
     text.forEach(function(t) {
       var childElement = document.createElement(child);
       childElement.innerText = t;
       parent.appendChild(childElement);
     });
     return parent;
  };

  return {
     renderSongList: renderSongList
  };

})();


var ajax = (function() {

   var getSongList = function() {
      var data;
      var xhr = new XMLHttpRequest();
      xhr.open('GET', 'http://localhost:3000/', true);
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.send('');
      xhr.onreadystatechange = function(rsp) {
         if (xhr.readyState === XMLHttpRequest.DONE){
            data = JSON.parse(xhr.response);
            console.log('kaksi');
            app.renderSongList(data);
         }
      };
   };

   return {
      getSongList: getSongList
   };

})();

ajax.getSongList();
