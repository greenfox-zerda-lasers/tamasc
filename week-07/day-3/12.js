'use strict';


var strings = {
  romanNum: ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'],
  latinNum: [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
  float2string: function (num) {
    return String(num);
  },
  string2float: function (num) {
    return parseFloat(num);
  },
  int2roman: function(num) {
    var i = 0;
    var roman = '';
    while (i < 13){
      if (num - this.latinNum[i] >= 0) {
        roman += this.romanNum[i];
        num -= this.latinNum[i];
      } else {
        i++;
      }
    }
    return roman;
  },
  roman2int: function(roman) {
    roman = roman.split('');
    var i = 0, l = roman.length, latin = 0;
    while (i < l) {
      if (i + 1 < l && this.romanNum.indexOf(roman[i]+roman[i+1]) != -1){
        latin += this.latinNum[this.romanNum.indexOf(roman[i]+roman[i+1])];
        i += 2;
      } else if (this.romanNum.indexOf(roman[i]) != -1) {
        latin += this.latinNum[this.romanNum.indexOf(roman[i])];
        i++;
      }
    }
    return latin;
  },
};

console.log(strings.int2roman(1534));
console.log(strings.roman2int('MCMXLI'));
