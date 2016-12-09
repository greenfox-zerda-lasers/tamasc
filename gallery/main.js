//  ***********************Generating jokes******************************

var jokes = [];
var object = [];


$(document).ready(function() {
  for (var j = 0; j < 6; j++){
    $.getJSON('http://api.icndb.com/jokes/random').then(function (e) {
       jokes.push(e.value.joke);
       if (jokes.length === 6){
         console.log('getting jokes ready');
       }
    });
  }
});

function generateData() {
   for (var i = 0; i < 6; i++){
      object[i]= {
        'id': i,
        'src': 'img/' + i + '.jpg',
        'title': 'Title'+i,
      };
   }
}

generateData();
//  ***********************Display**********************************


display();
var description = document.querySelector('.descriptionText');
console.log(description);

function display(){
  for (var k = 0, l = object.length; k < l; k++) {
    var image = document.createElement('img');
    image.setAttribute('src', object[k].src);
    image.setAttribute('id', object[k].id);
    image.setAttribute('title', object[k].title);
    if (k === 0) {
      image.classList.add('active');
    }
    document.querySelector('div .thumbnails').appendChild(image);
  }
  jokeParser();
}

var bigImage = document.querySelector('.bigImage');
bigImage.setAttribute('style', 'background: url(' + document.querySelector('.active').src + ')');

function jokeParser() {
  if (jokes[counter]) {
    description.innerHTML = jokes[counter];
  }
}

//  ***********************Functionality*****************************
var counter = parseInt(document.querySelector('.active').id);

function clickThumbnail() {
  document.querySelectorAll('.active').forEach(function(e){
    e.classList.remove('active');
  });
  this.classList.add('active');
  bigImage.setAttribute(
    'style', 'background: url(' + this.src + ')');
  counter = this.id;
  jokeParser();
}

function left() {
  slide(-1);
}

function right() {
  slide(1);
}

function slide(num) {
  document.querySelectorAll('.active').forEach(function(e){
     e.classList.remove('active');
   });
  counterUpdate(num);
  document.getElementById(counter).classList.add('active');
  bigImage.setAttribute(
    'style', 'background: url(' + document.getElementById(counter).src + ')');
  document.querySelector('.bigImage p').innerHTML = document.getElementsByClassName('active')[0].description;
  jokeParser();
  }

function counterUpdate(num) {
  if (counter + num > object.length-1){
    counter = 0;
  } else if (counter + num < 0) {
    counter = object.length -1;
  } else {
    counter += num;
  }
}


var thumbnails = document.querySelectorAll('.thumbnails img');
var buttons = document.querySelectorAll('button');
buttons[0].addEventListener('click', left);
buttons[1].addEventListener('click', right);
thumbnails.forEach(function(e) {
  e.addEventListener('click', clickThumbnail);
});

console.log('page load ready');
