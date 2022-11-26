def perms(x, y, z, n):
    import itertools
    # seen = set()
    # return sorted([l for l in [list(tup) for tup in list(itertools.permutations(list([a for a in range(x + 1)] + [b for b in range(y + 1)] + [c for c in range(z + 1)]), 3)) if "".join([str(d) for d in list(tup)]) not in seen and not seen.add("".join([str(d) for d in list(tup)]))] if sum(l) != n])
    a = [a for a in range(x + 1)]
    b = [b for b in range(y + 1)]
    c = [c for c in range(z + 1)]
    d = [a, b, c]
    #e = [a foor a in [d[i] for i in range(3)]]
    for a1 in a:
        for b1 in b:
            for c1 in c:
                if sum([a1, b1, c1]) != n:
                    print(a1, b1, c1)
        
    print(a, b, c)
    print(e)
    return permutations
 

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = perms(x, y, z, n)
    print(result)
