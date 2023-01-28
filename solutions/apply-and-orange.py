def compareTriplets(a, b):
    a_score = 0
    b_score = 0
    for n in range(3):
        if a[n] > b[n]:
            a_score += 1
        elif b[n] > a[n]:
            b_score += 1
    return "".join([str(a_score), str(b_score)])