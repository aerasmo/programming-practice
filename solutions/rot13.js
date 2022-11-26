function rot13(str) { 
    caps = []
    for (let i = 0; i < str.length; i++) {
      if (str.charCodeAt(i) < 97)
        caps.push(i)
    }
    str = str.toLowerCase()
    let alphabet = "abcdefghijklmnopqrstuvwxyz"
    let ciphered = ""
    for (let i = 0; i < str.length; i++) {
      let index = alphabet.indexOf(str[i])
      if  (index == -1) {
        ciphered += str[i]
      }
      else {
        if (index < 13) {
          ciphered += alphabet[index + 13]
        }
        else {
          ciphered += alphabet[index - 13]
        }
      }
    }
    ciphered = ciphered.split('')
    for (let i = 0; i < caps.length; i++) {
      ciphered[caps[i]] = ciphered[caps[i]].toUpperCase()
    }
    ciphered = ciphered.join('')
    return ciphered;
}

// rot13("EBG13 rknzcyr.") == "ROT13 example.";
// rot13("This is my first ROT13 excercise!" == "Guvf vf zl svefg EBG13 rkprepvfr!"