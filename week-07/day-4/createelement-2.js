(function(){
    // Remove the king from the list.
    document.querySelector('ul').removeChild(document.querySelector('li'));
    // Add 3 list items saying 'The Fox' to the list.
    var asteroidList = document.querySelector('ul');
    for (var i = 0; i < 3; i++) {
      var fox = document.createElement('li');
      fox.innerHTML = 'The Fox';
      asteroidList.appendChild(fox);
    }
})();
