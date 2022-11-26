# https://leetcode.com/problems/maximum-depth-of-binary-tree/
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# initial ans
def maxDepth(root: TreeNode) -> int:
    def dfs(node: TreeNode, depth: int) -> int:
        depth += 1
        x, y = 0, 0
        if ((not node.left) and (not node.right)):
            return depth
        if node.left:
            x = dfs(node.left, depth)
        if node.right:
            y = dfs(node.right, depth)
        return x if x > y else y
    return dfs(root, 0) if root else 0


# cleaner sol. 
def maxDepth(self, root: Optional[TreeNode]) -> int:
    def dfs(node: TreeNode, depth: int) -> int:
        if not node: 
            return depth
        return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))
    return dfs(root, 0) if root else 0