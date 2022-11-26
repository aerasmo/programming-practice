# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/

from typing import List

    
def twoSum(nums: List[int], target: int) -> List[int]:
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [l + 1, r + 1]
        if s > target:
            r -= 1
        else:
            l += 1
    return -1 