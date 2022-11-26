const prompt = require('prompt-sync')({sigint: true})

let len = prompt("l: ")
let wid = prompt("w: ")

const lwpa = (l, w) => {
    return {
        length: l,
        width: w,
        perimeter: 2 * l + 2 * w,
        area: l * w
    }
}
const rec = lwpa(len, wid);
console.log(rec.length)
console.log(rec.width)