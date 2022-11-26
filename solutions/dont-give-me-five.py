def dont_give_me_five(start,end):
    not_five = []
    for n in range(start, end + 1):
        s = str(n)
        if "5" not in s:
            not_five.append(n)
    return len(not_five)

# 1,9 -> 1,2,3,4,6,7,8,9 -> Result 8
# 4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> Result 12