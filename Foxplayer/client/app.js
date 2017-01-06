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
    ajax.getPlayLists();
    addEventsToButtons();
    addAudioEvents();
  };

  // *********Helper functions***********
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
    var current = document.querySelectorAll('.tracks tr')[counter]
    audio.src = current.src;
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

  var setActivePlayList = function (id) {
     var activeList = document.querySelector('.active-list');
     if (activeList) {
      activeList.classList.remove('active-list');
     }
     document.getElementById(id).classList.toggle('active-list');
     counter = 1;
     audio.src = '';
     imgPP.src = './img/play.svg';
     imgPP.classList = ['play'];
  }

  var togglePlayPause = function () {
    if (!audio.paused) {
      audio.pause();
      imgPP.src = './img/play.svg';
      imgPP.classList = ['play'];
    } else {
      audio.play();
      imgPP.src = './img/pause.svg';
      imgPP.classList = ['pause'];
    };
  };

  var filterSongs = function (songList, filterArray) {
    // console.log(songList, filterArray);      // complex filter
     return songList.filter( function (song) {
        return filterArray.indexOf(song.id) !== -1;
     });
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
      document.querySelector('#forward').click();
      audio.play();
    });
  };

  // **************View****************

  // var removeSong = function

  var renderHelper = function (child, text, parent) { //creates a HTML element and appends it to the given parent
    text.forEach(function (t) {
      var childElement = document.createElement(child);
      childElement.innerText = t;
      parent.appendChild(childElement);
    });
    var deleteIcon = document.createElement('p');
    deleteIcon.innerHTML = '  &#10005';
    parent.appendChild(deleteIcon);
    deleteIcon.addEventListener('click', function () {
      // console.log(this.parentElement.id);
      ajax.deleteSong(this.parentElement.id);
    })
    return parent;
  };

  var renderTable = function (items, tableClass, callback) {   //renders tables with the given parameters
    var row;
    var table = document.querySelector(tableClass);
    items.forEach(function (item, index) {
      row = document.createElement('tr');
      var firstTd = document.createElement('td');
      firstTd.innerText = index+1;
      row.appendChild(firstTd);
      callback(item, row);
      table.appendChild(row);
    })
  }

  var renderListItems = function (lists) {
    var allTracksRow = document.getElementById('list-0');
    allTracksRow.addEventListener('click', function () {
      setActivePlayList(allTracksRow.id);
      document.querySelector('.tracks').innerHTML = '';
      renderSongList(ajax.allSongs[0]);
    });
    var creator = function (list, row) {
      var textArray = [list.name];
      row.id = 'list-' + list.id;
      row.originId = list.id;
      row.addEventListener('click', function () {
         setActivePlayList(this.id);
         document.querySelector('.tracks').innerHTML = '';
         var currentPlayList = ajax.playLists[0].filter(function (item) {
            return item.id == row.originId;
         });
         console.log(currentPlayList);
         renderSongList(filterSongs(ajax.allSongs[0], currentPlayList[0].tracks));
      });
      row = renderHelper('td', textArray, row);
    };
    renderTable(lists, '.playlists', creator);
  }

  var renderSongList = function (songs) {
    var creator = function (song, row) {
      var textArray = [song.artist[0] +
        ' - ' + song.title, secToDuration(song.duration)];
      row.src = song.src;
      row.artist = song.artist;
      row.addEventListener('click', function () {
         counter = parseInt(this.id);
         setActive(counter);
         audio.src = this.src;
      });
      row = renderHelper('td', textArray, row);
      row.id = song.id;
    };
    renderTable(songs, '.tracks', creator);
  };

  var renderCurrentSong = function (currentSongText, artist) {
    var currentSongEl = document.querySelector('.song-info');
    currentSongEl.innerText = currentSongText;
    ajax.getArtistInfo(artist);
  };

  return {
    filterSongs: filterSongs,
    fire: fireApp,
    renderSongList: renderSongList,
    renderListItems: renderListItems
  };

})();


var ajax = (function () {
  var allSongs = [];
  var playLists = [];

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

  // var deleteSong = function (id) {
  //   var remove = function (data) {
  //     playLists[0][id].tracks = data.tracks;
  //     app.renderSongList(app.filterSongs(allSongs, data.tracks));
  //   };
  //   var playListId = document.querySelector('.active-list').id.slice(5);
  //   if (playListId == 0) {return}
  //   open('DELETE', 'http://localhost:3001/playlist-tracks/'+playListId+'/'+id, '', app.removeSong);
  // }

  var getPlayLists = function () {
    var renderPlayLists = function (data) {
      playLists.push(data);
      data.forEach(function (item, index) {
        var tracksArr = item.tracks.split(',');
        var tracksIntArr = [];
        tracksArr.forEach(function (item) {
          tracksIntArr.push(parseInt(item));
        })
        playLists[0][index]['tracks'] = tracksIntArr;
      })
      app.renderListItems(playLists[0]);
      console.log(playLists);
    };
    open('GET', 'http://localhost:3001/playlist', '', renderPlayLists);
  };

  var getSongList = function () {
    var renderSongList = function (data) {
      var songList = data.sort(function (a, b) {
        return a.id - b.id;
      });
      allSongs.push(songList);
      allSongs = allSongs[0];
      app.renderSongList(songList);
      return songList;
    };
    open('GET', 'http://localhost:3001/playlist-tracks', '', renderSongList)
  };

  var getArtistInfo = function (artist) {
    var changeImg = function (data) {
      imgArtist.src = data.artist.image[2]['#text'];
      if (!data.artist.image[2]['#text']) {
        imgArtist.src = 'https://raw.githubusercontent.com/greenfox-academy/teaching-materials/master/javascript/project-music-player/img/music-placeholder.png';
      }
    };
    var url = 'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=' + artist +
      '&api_key=ee125f318852fc7d1c2f4e21458a0035&format=json';
    open('GET', url, '', changeImg)
  };

  return {
    allSongs: allSongs,
    playLists: playLists,
    getSongList: getSongList,
    getPlayLists: getPlayLists,
    getArtistInfo: getArtistInfo,
    // deleteSong: deleteSong
  };

})();


app.fire();
