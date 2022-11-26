function formatDuration (seconds) {
  if (seconds == 0) return "now"
  let translated = []
  let conversion = {
    'year': 86400 * 365,
    'day': 86400,
    'hour': 3600,
    'minute': 60,
    'second': 1,
  }
  let data = {
    'year': 0,
    'day': 0,
    'hour': 0,
    'minute': 0,
    'second': 0,
  }
  for (let key in conversion) {
    while (seconds >= conversion[key]) {
        data[key] += 1
        seconds -= conversion[key]
      }
  }
  let postfix = ""
  for (let date in data) {
    postfix = ""
    if (data[date] >= 1) {
        if (data[date] > 1) postfix = "s"
        translated.push(`${data[date]} ${date + postfix}`)
    }
  }
  if (translated.length == 1)
    return translated[0]
  else if (translated.length == 2) {
    return translated.join(' and ')
  }
  
  else {
      let last_index = translated.length - 1
      return translated.slice(0, last_index).join(', ') + ' and ' + translated[last_index]
  }
}