const CONVERSION = [
    {"num": 1000, "roman": "M"},
    {"num": 900, "roman": "CM"},
    {"num": 500, "roman": "D"},
    {"num": 400, "roman": "CD"},
    {"num": 100, "roman": "C"},
    {"num": 90, "roman": "XC"},
    {"num": 50, "roman": "L"},
    {"num": 40, "roman": "XL"},
    {"num": 10, "roman": "X"},
    {"num": 9, "roman": "IX"},
    {"num": 5, "roman": "V"},
    {"num": 4, "roman": "IV"},
    {"num": 1, "roman": "I"},
]

const solution = (num) => {
let romanNumeral = ""
let val, roman
for (let i = 0; i < CONVERSION.length; i++) {
   val = CONVERSION[i]["num"]
   roman = CONVERSION[i]["roman"]
   while (num >= val) {
       romanNumeral += roman
       num -= val
   }
}
return romanNumeral
}