def rps(p1, p2):
    defi = ['rock', 'paper', 'scissors']
    
    i1 = defi.index(p1)
    i2 = defi.index(p2)
    
    result = "Draw!"

    if i1 == 0 and i2 == len(defi) - 1:
        result = "Player 1 won!"
    elif i1 == len(defi) - 1 and i2 == 0:
        result = "Player 2 won!"
    elif i1 > i2:
        result = "Player 1 won!"
    elif i2 > i1:
        result = "Player 2 won!"
    return result
