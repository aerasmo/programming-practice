def nb_dig(n, d):
    count = 0
    d = str(d)
    for i in range(n + 1):
        num = i ** 2 
        count += str(num).count(d)
    return count


# nb_dig(25, 1) returns 11 since
# the k*k that contain the digit 1 are:
# 1, 16, 81, 100, 121, 144, 169, 196, 361, 441.
# So there are 11 digits 1 for the squares of numbers between 0 and 25.