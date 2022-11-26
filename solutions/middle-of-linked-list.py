#https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        mid = head
        current = head
        while True:
            if (current.next):
                if (i % 2 == 0):
                    mid = mid.next
                current = current.next
            elif not current.next:
                return mid
            i+=1