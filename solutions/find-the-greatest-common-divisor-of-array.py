# gcd of min and max in an array
def findGCD(nums) -> int:
    min_ = min(nums)
    max_ = max(nums)
    
    for n in range(min_, 1, -1):
        if (min_ % n == 0) and (max_ % n == 0): # prime
            return n
    else:
        return 1