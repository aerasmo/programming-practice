from itertools import permutations


s, n = tuple(input().split(" "))
n = int(n)

for t in sorted(list(permutations(s, n))):
    print("".join(list(t)))