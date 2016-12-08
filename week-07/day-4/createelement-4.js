(function() {
    // Remove the king from the list.
    document.querySelector('ul').removeChild(document.querySelector('li'));
    // Fill the list based on the following list of objects:
    var planetData = [{
        category: 'inhabited',
        content: 'Foxes',
        asteroid: true
    }, {
        category: 'inhabited',
        content: 'Whales and Rabbits',
        asteroid: true
    }, {
        category: 'uninhabited',
        content: 'Baobabs and Roses',
        asteroid: true
    }, {
        category: 'inhabited',
        content: 'Giant monsters',
        asteroid: false
    }, {
        category: 'inhabited',
        content: 'Sheep',
        asteroid: true
    }];

    var asteroidAppender = function(planet) {
        if (planet.asteroid) {
            var item = document.createElement('li');
            item.innerHTML = planet.content;
            item.classList.add(planet.category);
            document.querySelector('ul').appendChild(item);
        }
    };

    planetData.forEach(asteroidAppender);
    // only add the asteroids to the list.
    // each list item should have its category as a class
    // and its content as text content.
})();
