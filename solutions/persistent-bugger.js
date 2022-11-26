function persistence(num, n = 0) {
    if (num.toString().length == 1)
      return n // recurion break
    n += 1  
    return persistence(num.toString().split('').reduce( (a,b) => a * b ), n)
 }