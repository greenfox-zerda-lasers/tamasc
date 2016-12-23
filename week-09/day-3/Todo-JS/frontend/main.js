'use strict';

var ul = document.querySelector('ul');

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
    }
  };
};


var addTodo = function () {
  var todoItem = {
    text: document.querySelector('input').value,
  };
  open('POST','http://localhost:3000/todos/',
  JSON.stringify(todoItem), listTodos);
};


var listTodos = function () {
  var callback = refresh;
  open('GET','http://localhost:3000/todos/',
  '', refresh);
};


var deleteTodo = function (id) {
  open('DELETE','http://localhost:3000/todos/'+id,
  '', listTodos);
};


var checkTodo = function (item) {
  var data = {
    text: item.innerText,
  };
  if (!item.className) {
    data.completed = true;
  } else {
    data.completed = false;
  }
  open('PUT','http://localhost:3000/todos/'+item.id,
  JSON.stringify(data), listTodos);
};


var refresh = function(data) {
      document.querySelector('ul').innerHTML = '';
   if (data) {
     data.reverse().forEach(function (e) {
       if (!e.text) {
         return;
       }
       var item = document.createElement('li');
       item.innerText = e.text;
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
       } else {
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

document.querySelector('input[type=button]').addEventListener('click', function(){
   addTodo();
   document.querySelector('form').reset();
});


window.onload = listTodos;

setInterval(function() {
  listTodos();
}, 2000);
