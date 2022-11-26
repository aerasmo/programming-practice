const maxSequence = (arr) =>{
    let max = 0
    for (let i = 0; i < arr.length; i++) {
      for (let j = 0; j < arr.length; j++) {
        sums = arr.slice(i, j + 1).reduce((a,b) => a + b, 0)
        if (sums > max) max = sums
      } 
    }
    return max
  }
  
//   The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

// maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
// should be 6: [4, -1, 2, 1]