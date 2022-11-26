const isPrime = num => {
    if (num <= 1) return false
    let s = Math.sqrt(num)
    for(let i = 2; i <= s; i++)
        if(num % i === 0) return false; 
    return true;
}