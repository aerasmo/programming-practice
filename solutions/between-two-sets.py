def getTotalX(a, b):
    factors = set()
    factors2 = set()
    #get factors
    for x in b:
        for n in range(1, x + 1):
            if (x % n == 0 and n <= min(b)):
                factors.add(n)
    #filter for both array
    for factor in factors:
        accepted = True
        for y in a:
            if (factor % y) != 0:
                accepted = False
        for x in b:
            if (x % factor != 0):
                accepted = False
        if accepted:
            factors2.add(factor)

    return len(factors2)