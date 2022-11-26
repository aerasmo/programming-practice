def last_survivor(letters, coords): 
    for i in coords:
        letters = letters[:i] + letters[i+1:]
    return letters

l = input()
a = list(map(int, input().split()))



print(last_survivor(l, a)) 