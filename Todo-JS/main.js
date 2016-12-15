'use strict'

document.querySelector('input[type=button]').addEventListener('click', function(){
   Ajax.getTodos();
});

var Ajax = function() {

};

Ajax.prototype.getTodos = function() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send();
  xhr.onreadystatechange = function(rsp) {
    if (xhr.readyState === XMLHttpRequest.DONE){
      console.log(JSON.parse(xhr.response));
    }
  };
}
