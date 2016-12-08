'use strict';

(function() {
    // Create a script that replaces every h1 headline's content
    // with 'Green Fox Academy Conquers the World'.
    var h1s = document.querySelectorAll('h1');
    var changeH1 = function(item) {
        item.innerHTML = 'Green Fox Academy Conquers the World';
    };

    h1s.forEach(changeH1);
    // Create a bookmarklet that does that on any website.
})();
