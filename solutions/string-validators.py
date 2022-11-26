def stringValidate(str):
    cons = [False for _ in range(5)]
    for char in str:
        if char.isalnum() and not cons[0]:
            cons[0] = True
        if char.isalpha() and not cons[1]:
            cons[1] = True
        if char.isdigit() and not cons[2]:
            cons[2] = True
        if char.islower() and not cons[3]:
            cons[3] = True
        if char.isupper() and not cons[4]:
            cons[4] = True
    [print(con) for con in cons]


if __name__ == '__main__':
    s = input()
    stringValidate(s)