# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def node_builder(arr) -> ListNode:
    head = ListNode(arr[0])
    m = head  
    for e in arr[1:]:
        m.next = ListNode(e)
        m = m.next

    return head

def node_printer(node: ListNode) -> None:
    print(node.val)
    while node.next:
        print(node.next.val)
        node = node.next

# floyds tortoise and hare 
def hasCycle(head: Optional[ListNode]) -> bool:
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


a = ListNode()
b = ListNode()
c = ListNode()

a.next = b
b.next = c

print(hasCycle(a))