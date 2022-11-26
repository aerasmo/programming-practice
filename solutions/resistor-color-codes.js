function decodeResistorColors(bands) {
    bands = bands.split(" ")
    let conversion = {
      'black': 0,
      'brown': 1,
      'red': 2,
      'orange': 3,
      'yellow': 4,
      'green': 5,
      'blue': 6,
      'violet': 7,
      'gray': 8,
      'white': 9
    }
    let first = conversion[bands[0]]
    let second = conversion[bands[1]]
    let exponent = conversion[bands[2]]
    let num = parseInt(first.toString() + second.toString()) * Math.pow(10, exponent)
    let last_band = {
      'gold': '5%',
      'silver': '10%'
    }
    
    let tolerance = (bands.length == 4 ? last_band[bands[3]] : '20%')
    let str = ""
    if (num >= 1000000) {
      str = (num / 1000000).toString() + 'M'
    }
    else if (num >= 1000) {
      str = (num / 1000).toString() + 'k'
    }
    else str = num.toString()
    let decoded = `${str} ohms, ${tolerance}`
    return decoded;
  }