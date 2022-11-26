from re import sub
from typing import List

def partitionArray(nums: List[int], k: int) -> int:
    if len(nums) <= 1:
        return 1

    nums = sorted(nums)
    l = 0
    r = 0
    subsequences = []

    while r < len(nums):
        min_so_far = min(nums[l:r+1])
        max_so_far = max(nums[l:r+1])
        diff = max_so_far - min_so_far
        prev_r = r

        if diff < k:
            r+=1
            min_so_far = min(nums[l:r+1])
            max_so_far = max(nums[l:r+1])
            diff = max_so_far - min_so_far
            if (r >= len(nums)):
                subsequences.append(nums[l:prev_r+1])
                break
        if diff > k:            
            subsequences.append(nums[l:prev_r+1])          
            l = r
        elif diff == k:
            try:
                while nums[r+1] == nums[r]:
                    r += 1
                subsequences.append(nums[l:r+1])
            except IndexError:
                subsequences.append(nums[l:r+1])
            r+=1
            l = r
    return len(subsequences)

print(partitionArray([3, 6, 1, 2, 5], 2))
print(partitionArray([1, 2, 3], 1))
print(partitionArray([2, 2, 4, 5], 0))