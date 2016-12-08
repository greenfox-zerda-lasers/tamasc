(function () {
  var items = ['apple', 'banana', 'cat', 'dog'];
  var listItems = document.querySelectorAll('li');
  for (var i = 0, l = listItems.length; i < l; i++){
    listItems[i].innerHTML = items[i];
  }
})();
