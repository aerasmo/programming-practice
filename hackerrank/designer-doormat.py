def mat(n, m):
    greeting ='WELCOME'
    fill = '-'
    design = '.|.'
    for r in range(n):
        if r < (n - 1) / 2:
            print((design * (2 * r + 1)).center(m, fill))
        elif r == (n - 1) / 2:
            print(greeting.center(m, fill))
        else:
            print((design * ((n - 2) - (2 * (r - int((n + 1)/ 2))))).center(m, fill))