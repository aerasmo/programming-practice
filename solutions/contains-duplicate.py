# https://leetcode.com/problems/contains-duplicate/
# 
# https://leetcode.com/problems/contains-duplicate/discuss/60858/Possible-solutions.
from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    if len(nums) <= 1: return False
    nums = sorted(nums)
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            return True
    return False

def contains_duplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))

contains_duplicate([1, 2 ,4, 1])
contains_duplicate([1, 1, 4, 1])
contains_duplicate([])
contains_duplicate([1])
contains_duplicate([1, 2, 4, 3])