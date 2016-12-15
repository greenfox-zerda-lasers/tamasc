'use strict';

// ***************Functionality******************

document.querySelector('input[type=button]').addEventListener('click', function(){
   ajax.getTodos();
});

var ul = document.querySelector('ul');

// ****************Ajax object*******************

var Ajax = function() {};

Ajax.prototype.getTodos = function() {
  var data;
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send();
  xhr.onreadystatechange = function(rsp) {
    if (xhr.readyState === XMLHttpRequest.DONE){
      data = JSON.parse(xhr.response).reverse();
      app.refresh(data);
    }
  };
};

var ajax = new Ajax();


// ****************App object*******************

var App = function() {};

App.prototype.refresh = function(data) {
   document.querySelectorAll('li').forEach(function(item) {
      ul.removeChild(item);
   });
   data.forEach(function (e) {
      var item = document.createElement('li');
      item.innerHTML = e.text;
      if (!e.completed) {
         item.className = 'completed';
      }
      ul.appendChild(item);
   });
};

var app = new App();
app.refresh(ajax.getTodos());
