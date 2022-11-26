def valid_perfect_square(x): 
    if x in (1, 4, 9):
        return True

    else:
        l = 0
        r = x
        while l <= r:
            mid = (l + r) // 2
            sqr = mid ** 2
            if sqr == x:
                return True
            if sqr > x:
                r = mid - 1
            elif sqr < x:
                l = mid + 1

    return False

print(valid_perfect_square(16))
print(valid_perfect_square(14))