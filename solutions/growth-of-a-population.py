def nb_year(p, percent, aug, target):
    year = 0
    while p < target:
        year += 1
        p += p * (percent / 100)
        p += aug
        p = int(p)
    return year