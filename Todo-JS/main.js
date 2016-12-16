'use strict';


var open = function(request, url, dataToSend, callback) {
  var data;
  var xhr = new XMLHttpRequest();
  xhr.open(request, url, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(dataToSend);
  xhr.onreadystatechange = function(rsp) {
    if (xhr.readyState === XMLHttpRequest.DONE){
      data = JSON.parse(xhr.response);
      callback(data);
      // listTodos();

    }
  };
};


var addTodo = function () {
  var todoItem = {
    text: document.querySelector('input').value,
  };
  open('POST','https://mysterious-dusk-8248.herokuapp.com/todos',
  JSON.stringify(todoItem), listTodos);
  listTodos();
};


var listTodos = function () {
  var callback = refresh;
  open('GET','https://mysterious-dusk-8248.herokuapp.com/todos',
  '', refresh);
};

var deleteTodo = function (id) {
  open('DELETE','https://mysterious-dusk-8248.herokuapp.com/todos'+'/'+id,
  '', listTodos);
};

var checkTodo = function (item) {
  var data = {
    text: item.innerHTML,
  };
  if (!item.className) {
    data.completed = true;
  } else {
    data.completed = false;
  }
  open('PUT','https://mysterious-dusk-8248.herokuapp.com/todos'+'/'+item.id,
  JSON.stringify(data), listTodos);
};

var refresh = function(data) {
   document.querySelectorAll('li').forEach(function(item) {
      ul.removeChild(item);
   });
   if (data) {
     data.reverse().forEach(function (e) {
       var item = document.createElement('li');
       item.innerHTML = e.text;
       item.id = e.id;
       var del = document.createElement('img');
       del.src = './delete.svg';
       del.className = 'delete';
       del.addEventListener('click', function() {
         deleteTodo(this.parentElement.id);
       });
       item.appendChild(del);
       var status = document.createElement('img');
       status.className = 'status';
       if (e.completed) {
         item.className = 'completed';
         status.src = './done.svg';
       } else if(!e.completed) {
         status.src = './notdone.svg';
       }
       status.addEventListener('click', function() {
         checkTodo(this.parentElement);
       });
       item.appendChild(status);
       ul.appendChild(item);
     });
   }
};

// ***************Functionality******************

document.querySelector('input[type=button]').addEventListener('click', function(){
   addTodo();
   document.querySelector('form').reset();
});

var ul = document.querySelector('ul');

window.onload = listTodos;
