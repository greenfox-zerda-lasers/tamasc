var bar = function() { console.log("bar"); }
var foo = function() { console.log("foo"); }
console.log("baz");
setTimeout(foo, 1000);
setTimeout(bar, 500);
