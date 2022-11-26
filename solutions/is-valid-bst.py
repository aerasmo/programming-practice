from utils.treenode import TreeNode
from typing import Optional
inp1 = input()

inps = inp1.split(" ")
arr1 = [int(s) if s.isdigit() else None for s in inps ]
root1 = TreeNode.nodeBuilder(arr1)

# def isValidBST(root: Optional[TreeNode]) -> bool:
#     def rootNodeLessThanCompare(root, node) -> bool:
#         if node:
#             if (node.left != None):
#                 if (node.left.val != None):
#                     if node.left.val >= root.val:
#                         return False
#             if (node.right != None):
#                 if (node.right.val != None):
#                     if node.right.val >= root.val:
#                         return False
#             l_valid = rootNodeLessThanCompare(root, node.left)
#             r_valid = rootNodeLessThanCompare(root, node.right)
#             return l_valid and r_valid
#         return True
#     def rootNodeGreaterThanCompare(root, node) -> bool:
#         if node:
#             if (node.left != None):
#                 if (node.left.val != None):
#                     if node.left.val <= root.val:
#                         return False
#             if (node.right != None):
#                 if (node.right.val != None):
#                     if node.right.val <= root.val:
#                         return False
#             l_valid = rootNodeGreaterThanCompare(root, node.left)
#             r_valid = rootNodeGreaterThanCompare(root, node.right)
#             return l_valid and r_valid

#         return True

#     def nodeChecker(root, node):
#         if node:
#             if (node.left != None):
#                 if (node.left.val != None):
#                     if node.left.val >= node.val:
#                         return False
#             if (node.right != None):
#                 if (node.right.val != None):
#                     if node.right.val <= node.val:
#                         return False
#             rnlt = rootNodeLessThanCompare(root, node)
#             rngt = rootNodeGreaterThanCompare(root, node)
#             valid_left = nodeChecker(root, node.left)
#             valid_right = nodeChecker(root, node.left)
#             return valid_left and valid_right and rnlt and rngt
#         else:
#             return True

#     def dfs(node) -> bool:
#         if node:
#             if (node.left != None):
#                 if (node.left.val != None):
#                     if node.left.val >= node.val:
#                         return False
#             if (node.right != None):
#                 if (node.right.val != None):
#                     if node.right.val <= node.val:
#                         return False
#             valid_left = True
#             valid_right = True
#             if node.left == None:
#                 return True
#             if node.right == None:
#                 return True
#             if node.left != None:
#                 valid_left = nodeChecker(node, node.left)
#                 d_left = dfs(node.left)
#             if node.right != None:
#                 valid_right = nodeChecker(node, node.right)
#                 d_right = dfs(node.right)
#             return d_left and d_right and valid_left and valid_right
#     return dfs(root)

# print(isValidBST(root1))

# CONCEDED - BEST SOL

def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
    if not root:  return True
    if root.val <= floor or root.val >= ceiling: return False
    return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)