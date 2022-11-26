def find_outlier(integers):
    l = integers[:3]
    odds = [n for n in l if n % 2 == 1]
    evens = [n for n in l if n % 2 == 0]
    return odds[0] if len(odds) > len(evens) else evens[0]
    
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)