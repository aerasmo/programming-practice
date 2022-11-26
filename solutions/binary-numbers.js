const prompt = require('prompt-sync')({sigint: true});

let n = prompt('input: ')

let arr = []

const conseqOnes = n => {
    
    let max = 0
    let maxHeight = 0
    while (n >= 1) {
        arr.push(n % 2)
        if (n % 2 == 1) {
            max += 1
        } else if (n % 2 == 0) {
            if (max > maxHeight) {
                maxHeight = max
            }
            max = 0
        }
        n = Math.floor(n / 2)

    } 
    // return maxHeight
    console.log(arr.reverse())
    return (max > maxHeight ? max : maxHeight)
}
console.log('conssq:', conseqOnes(n))
