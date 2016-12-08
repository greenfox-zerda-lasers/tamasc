'use strict';

(function() {
    // Create a script that replaces every image
    // with this: http://bit.ly/lpgreenfox
    var imgs = document.querySelectorAll('img');
    var changeImg = function(item) {
        item.setAttribute('src', 'http://bit.ly/lpgreenfox');
    };

    imgs.forEach(changeImg);
    // Create a bookmarklet that does that on any website.
})();
