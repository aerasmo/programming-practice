def printList(l):
    for item in l:
        print(item)

def staircase(n):
    staircase = []
    for x in range(1, n+1):
        stair = '#' * x
        staircase.append(stair.rjust(n))
    printList(staircase)