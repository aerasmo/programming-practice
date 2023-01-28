def birthday(s, d, m):
    l = 0
    for x in range(len(s)):
        temp = [s[x]]
        for y in range(x+1, len(s)):
            temp.append(s[y])
            if len(temp) >= m:
                break
        if sum(temp) == d:
            l+=1
    return l