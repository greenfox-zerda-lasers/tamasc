// 1. store the element that says 'The King' in the 'king' variable.
// console.log it.
var king = document.getElementById('b325');
// console.log(king);
// 2. store the element that contains the text 'The Conceited Man'
// in the 'conceited' variable.
// show the result in an 'alert' window.
var conceited = document.getElementsByClassName('b326');
var conceited2 = document.querySelector('.b326, .asteroid');
// alert(conceited);
// console.log(conceited);
// console.log(conceited2);
// 3. store 'The Businessman' and 'The Lamplighter'
// in the 'businessLamp' variable.
// console.log each of them.
var businessLamp = document.getElementsByClassName('big');
console.log(businessLamp[0], businessLamp[1]);
// 4. store 'The King' and 'The Conceited Man'
// in the 'conceitedKing' variable.
// alert them one by one.
var conceitedKing = document.querySelectorAll('.b326, #b325');
// for (var i = 0, l = conceitedKing.length; i < l; i++){
//   alert(conceitedKing[i]);
// }
// 5. store 'The King', 'The Conceited Man' and 'The Lamplighter'
// in the 'noBusiness' variable.
// console.log each of them.
var noBusiness = document.querySelectorAll('#b325, .b326, .b329');
for (var i = 0, l = noBusiness.length; i < l; i++){
  console.log(noBusiness[i]);
}
// 6. store 'The Businessman' in the 'allBizniss' variable.
// show the result in an 'alert' window.
var allBizniss = document.querySelector('p');
alert(allBizniss.innerHTML);
