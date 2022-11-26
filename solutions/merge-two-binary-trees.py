#https://leetcode.com/problems/merge-two-binary-trees/
from re import L
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1 and not root2: return None
    ans = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
    ans.left = mergeTrees(root1 and root1.left, root2 and root2.left)
    ans.right = mergeTrees(root1 and root1.right, root2 and root2.right)
    return ans


# def mergeTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    # if not root1: return root2
    # if not root2: return root1
    # return TreeNode(root1.val + root2.val, self.mergeTrees(root1.left, root2.left), self.mergeTrees(root1.right, root2.right))


def nodeBuilder(arr):
    if len(arr) == 0: return None
    root = TreeNode(arr[0])
    nodes = [root]
    i = 1
    diff = 1
    while i < len(arr):
        node = TreeNode(arr[i])
        if i % 2 == 1:
            nodes[i-diff].left = node
            diff += 1
        else: 
            nodes[i-diff].right = node
        nodes.append(node)
        i += 1
    return nodes[0]

inp1 = input()
inp2 = input()
arr1 = list(map(int, inp1.split(" ")))
arr2 = list(map(int, inp2.split(" ")))
print(arr1)
print(arr2)
root1 = nodeBuilder(arr1)
root2 = nodeBuilder(arr2)
root3 = mergeTrees(root1, root2) 
print(root3.val)
print(root3.left.val)
# print(root3.right.val)


# root1 = nodeBuilder([1,3,2,5])
# root2 = nodeBuilder([2,1,3,None,4,None,7])
# print(root1.left.left.val)
# print(root2.left.right.val)
# print(root2.right.right.val)