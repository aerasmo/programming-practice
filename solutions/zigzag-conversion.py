# class Solution:
def convert(s, n):
    if n == 1: return s
    f = (n - 1) * 2
    m = n - 2
    rows = [""] * n
    for i in range(len(s)):
        modf = i % f 
        if modf < n:
            rows[modf] += s[i]
        else:
            rows[m - modf] += s[i]
    return "".join(rows)

inputs = input().split()
print(convert(inputs[0], int(inputs[1])))
        