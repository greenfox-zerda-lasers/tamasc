(function () {
  // fill every paragraph with the last one's content.
  var piz = document.querySelectorAll('p');
  var text = piz[piz.length - 1].innerHTML;
  console.log(piz, text);
  var jajjj = function(e) {e.innerHTML = text;};
  piz.forEach(jajjj);
})();
