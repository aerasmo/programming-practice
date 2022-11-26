def permutations(n):
    perms = []
    for i in range(len(n)):
        # if i == len(n) - 1:
            # break
        for j in range(len(n)):
            if i == j:
                continue
                # break
            cur_perms = [n[i]] + [None ] * (len(n) - 1)
            for k in range(len(n)):
                if k == i:
                    continue
                # print(k)
                # print(n[k])
                # if j == k:
                    # continue
                cur_perms[k] = n[j]
            # cur_perms = [i]
                print(cur_perms)
    return perms
        

n = list(map(int, input().split()))
print(permutations(n))
