def minion_game(string):
    s = 0
    k = 0

    for i in range(len(string)):

        if string[i] in 'AEIOU': 
            k += len(string) - i
        else:
            s += len(string) - i

    if k > s:
        output = f'Kevin {k}'
    elif s > k:
        output = f'Stuart {s}'
    else:
        output = 'Draw'
    print(output)