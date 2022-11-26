let conversion = {
    0: 'black',
    1: 'brown',
    2: 'red',
    3: 'orange',
    4: 'yellow',
    5: 'green',
    6: 'blue',
    7: 'violet',
    8: 'gray',
    9: 'white',
  }

function encodeResistorColors(ohmsString) {
    let codes = []
    let inputs = ohmsString.split(' ')
    let charge = inputs[0]
    let first = ""
    let second = ""
    if (charge.indexOf("M") !== -1) {
      charge = charge.replace("M", "")
      charge = parseFloat(charge) * Math.pow(10, 6)
    }

    else if (charge.indexOf("k") !== -1) {
      charge = charge.replace("k", "")
      charge = parseFloat(charge) * Math.pow(10, 3)
    }
    else {
        charge = parseFloat(charge)
    }
    first = charge.toString()[0]
    second = charge.toString()[1]
    third = charge.toString().length - 2
    charge = charge / Math.pow(10, third)
    third = third.toString()

    codes = [conversion[first], conversion[second], conversion[third], "gold"]
    return codes.join(' ')
}