# def moveZeroes(nums):
#     l, r = 0, len(nums) - 1

#     while l != r:
#         print(l, r)
#         if nums[l] == 0:
#             nums.append(nums.pop(l))
#             r -= 1
#         else:
#             if nums[r] == 0:
#                 nums.append(nums.pop(r))
#             l += 1

# tortoise and hare algo
def moveZeroes(nums: list) -> None:
    slow = 0
    for fast in range(len(nums)):
        # 0, 1, 2, 3, 4
        if nums[fast] != 0 and nums[slow] == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        # wait while we find a non-zero element to
        # swap with you
        if nums[slow] != 0:
            slow += 1
        print(nums)
moveZeroes([0,1,0,3,12])
moveZeroes([0,0, 1])
