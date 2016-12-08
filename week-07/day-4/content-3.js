  // fill output1 with the first paragraph's content, text only.
  document.querySelectorAll('p')[1].innerHTML = document.querySelector('p').textContent;
  // fill output2 with the first paragraph's content keeping the cat strong.
  document.querySelectorAll('p')[2].innerHTML = document.querySelector('p').innerHTML;
