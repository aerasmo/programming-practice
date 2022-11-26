from itertools import combinations
# doesnt care about the order in general 

s, n = tuple(input().split(" "))

n = int(n)

for i in range(1, n+1):
    res = []
    for t in sorted(list(combinations(s, i))):
        res.append("".join(sorted(list(t))))
        
    for s_ in sorted(res):
        print(s_)