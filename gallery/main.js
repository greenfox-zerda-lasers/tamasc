'use strict';

$.ajaxSetup({cache: false});

function generateData() {
   var object = [];
   for (var i = 0; i < 5; i++){
      var jokeString;
      object[i]= {'src': 'https://unsplash.it/g/600/400?random', 'description': getJoke()}
   }
   console.log(object[0]);
}

function getJoke() {
   return $.getJSON('http://api.icndb.com/jokes/random', function(joke) {console.log(typeof joke['value']['joke']);return joke.value.joke});
}



var bigImage = document.querySelector('.bigImage');

var buttons = document.querySelectorAll('button');

var loadNext = function() {
   console.log('click');
   var image = document.createElement('img');
   image.setAttribute('src', 'https://source.unsplash.com/600x400');
   document.querySelector('.bigImage').appendChild(image);
};
buttons[0].addEventListener('click', generateData);
