# https://leetcode.com/problems/search-insert-position/submissions/
from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    if target < nums[low]:
        return 0
    if target > nums[high]:
        return len(nums)
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return low

def searchInsert(nums: List[int], target: int) -> int:
    low, high = 0, len(nums)
    while low < high:
        mid = (low + high) // 2
        if target > nums[mid]:
            low = mid + 1
        else:
            high = mid
    return low