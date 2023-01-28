def divisibleSumPairs(n, k, ar):
    l = 0
    for x in range(n):
        for y in range(x+1, n):
            s = ar[x] + ar[y]
            if s % k == 0:
                l += 1
    return l