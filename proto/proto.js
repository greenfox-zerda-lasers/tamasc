var Food = function(type) {
   this.type = type;
   this.something = 15;
};

Food.prototype.eat = function(){
   console.log('you ate the ' + this.type);
};
//
var waffle = new Food('waffle');

console.log(waffle.something);

Food.something = 'asdasd'

console.log(waffle.something);

var cookie = new Food('cookie');

console.log(Food);
console.log(cookie.something);
