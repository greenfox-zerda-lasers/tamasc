var candyTime = 1000;
var candy = 0;
var lollypop = 0;

var showCandies = document.querySelector('.candies');
var showLollypops = document.querySelector('.lollypops');
var showSpeed = document.querySelector('.speed');
showLollypops.style.height = '20px';

var candyButton = document.querySelector('.create-candies');
var lollypopButton = document.querySelector('.buy-lollypops');
var candymachineButton = document.querySelector('.candy-machine');
showSpeed.innerHTML = 0;

var T;
var start = function() {T = setInterval(function(){
    if (lollypop > 9) {
      candy += Math.floor(lollypop/10);
      showCandies.innerHTML = candy;
      showSpeed.innerHTML = 1000/candyTime;
    }
  }, candyTime);
};

candyButton.addEventListener('click', function() {
  candy += 10;
  showCandies.innerHTML = candy;
});

lollypopButton.addEventListener('click', function() {
  if (candy > 9) {
    candy -= 1;
    lollypop += 1;
    showCandies.innerHTML = candy;
    showLollypops.innerHTML += '🍭';
    start();
  }
});

candymachineButton.addEventListener('click', function() {
  if (lollypop > 9) {
    candyTime /= 2;
  }
  clearTimeout(T);
  start();
});
