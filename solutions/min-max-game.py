from typing import List

def min_max_game(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    
    new_nums = []
    for i in range(len(nums)):
        try:
            if i % 2 == 0:
                new_nums.append(min(nums[2*i], nums[2*i+1]))
            else:
                new_nums.append(max(nums[2*i], nums[2*i+1]))
        except IndexError:
            break

    return min_max_game(new_nums)

n = list(map(int, input().split()))
print(min_max_game(n))