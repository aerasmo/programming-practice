def findMaxConsecutiveOnes(nums):
    mx = 0
    cr = 0
    
    for i in range(len(nums)):
        if (nums[i] == 1):
            cr += 1
            if cr > mx:
                mx = cr
        else:
            cr = 0
    return mx