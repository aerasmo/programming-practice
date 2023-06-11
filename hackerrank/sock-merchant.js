function sockMerchant(n, ar) {
    let counted = []
    let sockTotals = []
    ar.forEach(sock => {
        if (!(counted.includes(sock))) {
            sockTotals.push(ar.filter(n => n == sock).length)
            counted.push(sock)
        }
    })
    let totalPairs = 0
    sockTotals.forEach(total => {
        totalPairs += Math.floor(total / 2)
    }) 
    return totalPairs
}