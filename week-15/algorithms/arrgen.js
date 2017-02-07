const fs = require('fs');

let arr = [];

for (let i = 0; i < 5000; i++) {
  arr.push(i);
  arr.push(i);
}

const insert = `const array = [${arr}];
module.exports = array;`


fs.writeFile("algorithms/array.js", insert, function(err) {
    if(err) {
        return console.log(err);
    }
    console.log("The file was saved!");
});
