// 1. Alert the content of the heading.
var h = document.getElementsByTagName('H1')[0];
console.log(h);
// alert(h.innerHTML);
// 2. Write the content of the first paragraph to the console.
var pFirst = document.querySelector('p');
console.log('first p: ' + pFirst.innerHTML);
// 3. Alert the content of the second paragraph.
var pLast = document.querySelectorAll('p')[document.querySelectorAll('p').length-1];
console.log('last p: ' + pLast.innerHTML);
// 4. Replace the heading's content with 'New content'.
h.innerHTML = 'New content';
// 5. Replace the last paragraph's content with the first paragraph's content.
pLast.innerHTML = pFirst.innerHTML;
