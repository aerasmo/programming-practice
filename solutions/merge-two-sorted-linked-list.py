# Definition for singly-linked list.
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

def mergeTwoLists(n: Optional[ListNode], m: Optional[ListNode]) -> Optional[ListNode]:
    merged_node: ListNode = None
    nrun: bool = True
    mrun: bool = True

    if n and m:
        if n.val < m.val:
            merged_node = n

            if n.next: n = n.next
            else: nrun = False
        else:
            merged_node = m

            if m.next: m = m.next
            else: mrun = False
    elif n:
        merged_node = n

        if n.next: n = n.next
        else: nrun = False 
        mrun = False
    elif m:
        merged_node = m
        if m.next: m = m.next
        else: mrun = False
        nrun = False

    o = merged_node
    while (nrun or mrun):
        if (nrun and mrun):
            if n.val < m.val:   
                o.next = n
                if n.next: n = n.next
                else: nrun = False
            else:
                o.next = m
                if m.next: m = m.next
                else: mrun = False
        elif nrun:
            o.next = n
            if n.next: n = n.next
            else: nrun = False
        elif mrun:
            o.next = m
            if m.next: m = m.next
            else: mrun = False
        o = o.next

    return merged_node

arr = [1, 3, 5]
arr2 = [1, 2, 3, 5]

node = node_builder(arr)
node2 = node_builder(arr2)


node_printer(node)

print("---")

node_printer(node2)

print("---")

merged_node = mergeTwoLists(node, node2)
node_printer(merged_node)