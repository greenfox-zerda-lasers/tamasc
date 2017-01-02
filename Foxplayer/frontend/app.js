'use strict';

var ajax = (function() {
  var list = function(callback) {
    var data;
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:3000/', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(dataToSend);
    xhr.onreadystatechange = function(rsp) {
      if (xhr.readyState === XMLHttpRequest.DONE){
        data = JSON.parse(xhr.response);
        callback(data);
      }
    };
  };
})();

var render = (function() {
  var list = function () {
    
  }
})();
