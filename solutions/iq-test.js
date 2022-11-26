function iqTest(numbers){
    numbers = numbers.split(' ').map(x => parseInt(x))
    let evens = 0, odds = 0
    let last_odd = 0, last_even = 0
    for (let i = 0, n = 0; i < numbers.length; i++) {
      n = numbers[i]
      if ((n % 2 == 0)){
        if (odds > 1) return i + 1
        last_even = i
        evens += 1
      }
      else if ((n % 2 == 1)){
        if (evens > 1) return i + 1
        odds += 1
        last_odd = i
      }
    }
    if (evens > odds) return last_odd + 1
    else return last_even + 1
  }
  