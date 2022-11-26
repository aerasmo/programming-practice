def last_digit(n1, n2):
    if n2 == 0 or n1 == 1: return 1
    elif n1 == 5: return 5
    elif n2 == 6: return 6
    else:
        n = int(str(n1)[-1])
        b = n2 % 4
        if b == 0: b = 4
    
    return int(str(n ** b)[-1])