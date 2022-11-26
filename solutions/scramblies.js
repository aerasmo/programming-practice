function scramble(str1, str2) {
    const len1 = str1.length
    const len2 = str2.length
    
    if (len1 < len2) return false
  
    const counts = Array(26).fill(0)
    for (let i = 0; i < len2; i++) {
      counts[str2.charCodeAt(i) - 97]++
    }
    
    for (let i = 0, j = len2; i < len1; i++) {
      const chr1 = str1.charCodeAt(i) - 97
      const num2 = counts[chr1]
      
      if (num2) {
        if (--j === 0) return true
        
        counts[chr1]--
      }
    }
    return false
  }

// Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

// Notes:

// Only lower case letters will be used (a-z). No punctuation or digits will be included.
// Performance needs to be considered
// scramble('rkqodlw', 'world') ==> True
// scramble('cedewaraaossoqqyt', 'codewars') ==> True
// scramble('katas', 'steak') ==> False