(function() {
    // On the click of the button,
    // Count the items in the list
    // And display the result in the result element.
    var button = document.querySelector('button');
    var count = function() {
        var itemNum = document.querySelectorAll('li').length;
        document.querySelector('.result').innerHTML = itemNum;
    };
    button.addEventListener('click', count);
})();
