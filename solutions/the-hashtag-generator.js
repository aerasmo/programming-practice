function generateHashtag (str) {
    arr = str.split(' ').filter(x => x != '')
    if (!arr.length) return false
  
    String.prototype.capitalize = function() {
      return this.charAt(0).toUpperCase() + this.slice(1); 
    }
    for (let i = 0; i < arr.length; i++) {
      let word = arr[i].capitalize();
      arr[i] = word
    }
    hashtag = '#'+ arr.join('')
    if (hashtag.length > 140) 
      return false
    return hashtag
}

// Here's the deal:

// It must start with a hashtag (#).
// All words must have their first letter capitalized.
// If the final result is longer than 140 chars it must return false.
// If the input or the result is an empty string it must return false.
// " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
// "    Hello     World   "                  =>  "#HelloWorld"
// ""                                        =>  false