// Write the image's url to the console.
var imageSrc = document.querySelector('img').getAttribute('src');
console.log(imageSrc);
// Replace the image with a picture of yourself.
document.querySelector('img').setAttribute('src', 'https://scontent-frt3-1.xx.fbcdn.net/v/t1.0-1/c0.46.100.100/p100x100/11249016_967346833287114_4507466786678351248_n.jpg?oh=e01fff6d25ca2e526d7fd514f1092ff3&oe=58B77ABF');
// Make the link point to the Green Fox Academy website.
document.querySelector('a').setAttribute('href', 'http://www.greenfoxacademy.com/');
// Disable the second button.
var button2 = document.querySelectorAll('button')[1];
button2.setAttribute("disabled", 'true');
// Replace its text with 'Don't click me!'.
button2.innerHTML = 'Don\'t click me!'
