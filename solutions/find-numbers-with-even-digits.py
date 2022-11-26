def findNumbers(nums):
    t = 0
    for x in nums:
        if (len(str(x)) % 2 == 0):
            t += 1
    return t