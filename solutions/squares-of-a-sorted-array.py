#https://leetcode.com/problems/squares-of-a-sorted-array/

# A double-ended queue, or deque, has the feature of adding and removing elements from either end. The Deque module is a part of collections library. It has the methods for adding and removing elements which can be invoked directly with arguments.

import collections
from typing import List


# check left and right 
# the greater one will move to the left of queue
# pointer will move 

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        squares = collections.deque()
        while l <= r:
            lval, rval = abs(nums[l]), abs(nums[r])
            if lval > rval:
                squares.appendleft(lval ** 2)
                l += 1
            else:
                squares.appendleft(rval ** 2)
                r -= 1
        return list(squares)
