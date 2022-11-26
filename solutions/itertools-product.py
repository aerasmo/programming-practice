from itertools import product

a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))

SET_ = [a, b]
res = []

# for x, y in list(product([a], [b])):
for x, y in list(product(*SET_)):
    res.append("({}, {})".format(x, y))
    
print(" ".join(res))