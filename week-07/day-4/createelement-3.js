(function(){
    // Remove the king from the list.
    document.querySelector('ul').removeChild(document.querySelector('li'));
    // Add list items that have the following text contents:
    var items = ['apple', 'bubble', 'cat', 'green fox'];
    for (var i = 0, l = items.length; i < l; i++) {
      var item = document.createElement('li');
      item.innerHTML = items[i];
      document.querySelector('ul').appendChild(item);
    }
})();
