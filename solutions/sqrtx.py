def sqrt(x):
    l = 0
    r = x
    while l <= r:
        mid = (l + r) // 2
        sqr = mid ** 2
        if sqr == x:
            return mid
        elif sqr > x:
            r = mid - 1
        else:
            l = mid + 1
    return r
    
print(sqrt(9))