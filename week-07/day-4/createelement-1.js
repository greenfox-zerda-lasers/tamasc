(function() {
  // Add an item that says 'The Green Fox' to the asteroid list.
  var asteroidList = document.querySelector('ul');
  console.log(asteroidList);
  var greenFox = document.createElement('li');
  greenFox.innerHTML = 'The Green Fox';
  asteroidList.appendChild(greenFox);
  // Add an item that says 'The Lamplighter' to the asteroid list.
  var lampLighter = document.createElement('li');
  lampLighter.innerHTML = 'The Lamplighter';
  asteroidList.appendChild(lampLighter);
  // Add a heading saying 'I can add elements to the DOM!' to the .container.
  var contHeading = document.createElement('H1');
  contHeading.innerHTML = 'I can add elements to the DOM!';
  document.querySelector('.container').appendChild(contHeading);
  // Add an image, any image, to the container.
  var image = document.createElement('img');
  image.setAttribute('src', 'https://i.ytimg.com/vi/3YJpUROvQAk/maxresdefault.jpg');
  image.setAttribute('width', '50%');
  document.querySelector('.container').appendChild(image);
})();
