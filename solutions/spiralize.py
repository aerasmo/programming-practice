# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/train/python

def move(i, j, direction, scope=1):
    if direction == 0: #right
        return i, j + scope
    if direction == 1: #down
        return i + scope, j
    if direction == 2: #left
        return i, j - scope
    if direction == 3: #up
        return i - scope, j

def change_dir(direction):
    direction += 1
    if direction >= 4:
        direction = 0
    return direction 

def spiralize(size):
    # Generate empty array
    arr = []

    for i in range(size):
        arr.append([0 for i in range(size)])
    
    # initialize
    i, j = (0, 0)
    arr[i][j] = 1

    # going right
    direction = 0
    changed_prev = False

    while True:

        prev_i, prev_j = i, j
        i, j = move(i, j, direction)
        # check further in advance
        i1, j1 = move(i, j, direction, 1)   
        i2, j2 = move(i, j, direction, 2)

        if ((i1 < size) and (j1 < size))\
            and ((i1 >= 0) and (j1 >= 0)):
            if (arr[i1][j1] == 1):
                break

        if ((i < size) and (j < size))\
            and ((i >= 0) and (j >= 0)):
                arr[i][j] = 1
                prev_i, prev_j = i, j
                changed_prev = False

        else:
            direction = change_dir(direction)
            i, j = prev_i, prev_j
            if changed_prev == True: break
            changed_prev = True

        if ((i2 < size) and (j2 < size))\
            and ((i2 >= 0) and (j2 >= 0)):
            if (arr[i2][j2] == 1):
                direction = change_dir(direction)
                if changed_prev == True: break
                changed_prev = True
            else:
                changed_prev = False
                # print(i, j)
    # # viewing result
    # for l in arr:
    #     print(l)

    return arr

x = int(input())
print(spiralize(x))