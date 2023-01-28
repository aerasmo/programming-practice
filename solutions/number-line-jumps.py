def kangaroo(x1, v1, x2, v2):
    sameLocation = "NO"
    while True:
        if (x1 == x2):
            sameLocation = "YES"
            break

        elif (x2 > x1 and v2 >= v1) or (x1 > x2 and v1 >= v2):
            break

        x1 += v1
        x2 += v2
    return sameLocation