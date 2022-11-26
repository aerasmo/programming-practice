function highAndLow(numbers){
    numbers = numbers.split(" ")
    console.log(numbers)
    let low = parseInt(numbers[0])
    let high = parseInt(numbers[0])
    for (let i = 1; i < numbers.length; i++) {
      
      number = parseInt(numbers[i])
      if (number < low) {
        low = number
      }
      if (number > high) {
        high = number
      }
    }
    return high.toString() + " " + low.toString()
  }